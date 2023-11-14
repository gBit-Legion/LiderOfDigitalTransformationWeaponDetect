import json
import logging
import os.path

from fastapi import FastAPI, Request, routing, UploadFile
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.routing import APIRoute

from Services.CameraVideoCapture import RTSPCamera
from Services.CodesForInteraction import *

from Database.querry_to_database import *

logging.basicConfig(level=logging.INFO)

app = FastAPI()

app.mount("/static", StaticFiles(directory="./Frontend/yolo"), name='static')

# Создаем новый маршрут для наших статических файлов
static_router = routing.APIRouter(route_class=APIRoute)
static_router2 = routing.APIRouter(route_class=APIRoute)

app.include_router(static_router)
app.include_router(static_router2)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/serve/{camera_id}")
async def get_video_stream(camera_id: int):
    url = [
        "rtsp://admin:A1234567@188.170.176.190:8025 /Streaming/Channels/101?transportmode=unicast&profile=Profile_1"
    ]

    camera = RTSPCamera(url, "./labels", "./images")
    return StreamingResponse(camera.process_video(), media_type="multipart/x-mixed-replace; boundary=frame")


# @app.post("/getlist")
# async def get_list_checked_file(req: Request):
#     json_data = await req.json()
#     print(json_data)
#     return {"good": json_data}
#

@app.post('/excel')
async def file_uploader(file: UploadFile):
    if not os.path.exists("./upload"):
        os.makedirs("./upload")
        print("Папка успешно создана!")
    else:
        print("Папка уже существует.")
    print(file.filename)
    file_path = Path("./upload", file.filename)
    print(file_path)
    try:
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        url_id_list = add_in_dataset(f"./upload/{file.filename}")
        os.remove("./upload/{file.filename}")
        return {"message": url_id_list}

    except Exception as e:
        return {"message": e.args}


@app.post("/archive")
async def archive_upload(file: UploadFile):
    print(0)
    if not os.path.exists("./archive"):
        os.makedirs("./archive")
    if not os.path.exists("./image"):
        os.makedirs("./image")
    if not os.path.exists("./labels"):
        os.makedirs("./labels")
    if not os.path.exists("./video"):
        os.makedirs("./video")
    # logging.INFO("Папки успешно созданы")
    file_path = os.path.join("/archive", file.filename)

    result_list = []
    print(1)
    try:
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        unarchived(file_path)
        try:
            list_dir = os.listdir("./video")

        except Exception as e:
            # logging.WARNING({e.args}, {os.listdir("./video")})
            return {"directory_video_is_empty": e.args}

        for file in list_dir:
            # logging.INFO(f"file name: {file}")
            url = f"/processed_video/{file}"
            # logging.INFO(f"This is url: {url}")

            if not os.path.exists("./labels"):
                os.makedirs("./labels")

            image_dir = os.listdir(os.path.join("./image", os.path.splitext(file)[0]))
            labels_dir = os.listdir(os.path.join("./labels", os.path.splitext(file)[0]))

            # logging.INFO(f"image directory: {image_dir}, labels director: {labels_dir}")

            result_image = []
            img_list = []
            label_list = []

            if len(image_dir) != 0:
                for image, label in zip(image_dir, labels_dir):

                    with open(os.path.join((os.path.join("./labels", os.path.splitext(file)[0])), label), 'r') as file1:

                        for line in file1:
                            first_part = line.split(' ', 1)[0]
                            if first_part == '0':
                                label_list.append("knife")
                            elif first_part == '1':
                                label_list.append("pistol")
                            elif first_part == '2':
                                label_list.append("gun")
                            elif first_part == '3':
                                label_list.append("riffle")

                    result_image = {"image_name": os.path.splitext(image)[0],
                                    "image_url": f"/processed_image/{os.path.splitext(file)[0]}/{image}",
                                    "class_name": label_list
                                    }

                    img_list.append(result_image)
                    # logging.INFO(f"json part image list: {img_list}")
            else:
                result_image = {
                    "image_name": "no_weapon_detected",
                    "image_url": 0,
                    "class_name": "no_weapon_detected"
                }

                img_list.append(result_image)

            result_list.append({"url": url, "images": img_list})

            # logging.INFO(f"finally json: {result_list}")

        return json.dumps(result_list)
    except Exception as e:
        return {"message": e.args}


@static_router.get("/processed_video/{filename}")
def get_static_file(filename: str):
    if not os.path.exists("./video"):
        os.makedirs("./video")
        print("Папка успешно создана!")
    else:
        print("Папка уже существует.")

    # Определите путь к файлу на сервере FastAPI
    file_path = os.path.join("./video", filename)
    print(file_path)

    return FileResponse(file_path)


@static_router2.get("/processed_image/{video_name}/{filename}")
def get_static_image(filename: str, video_name: str):
    if not os.path.exists("./image"):
        os.makedirs("./image")

    # Определите путь к файлу на сервере FastAPI
    file_path = os.path.join("./image", os.path.join(video_name, filename))

    return FileResponse(file_path)
