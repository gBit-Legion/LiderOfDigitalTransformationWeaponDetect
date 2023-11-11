import json
import os

import cv2
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request, routing, WebSocket
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import UploadFile
from pathlib import Path

from fastapi.routing import APIRoute
from starlette.responses import StreamingResponse

from Services.CameraVideoCapture import RTSPCamera
from Services.CodesForInteraction import *
from Database.querry_to_database import *

app = FastAPI()

app.mount("/static", StaticFiles(directory="./Frontend/yolo"), name='static')

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

stop_stream = False


async def video_stream(websocket: WebSocket, rtsp_url: str):
    await websocket.accept()

    video_capture = cv2.VideoCapture(rtsp_url)

    while True:
        ret, frame = video_capture.read()

        if not ret:
            break

        # Преобразуем кадр в формат JPEG
        _, buffer = cv2.imencode('.jpg', frame)

        # Преобразуем кадр в строку base64
        frame_data = buffer.tobytes()

        # Отправляем кадр на фронтенд
        await websocket.send(frame_data)

    video_capture.release()


@app.websocket("//serve/{camera_id}")
async def video_feed(websocket: WebSocket, camera_id: int):
    rtsp_url = ["rtsp://admin:A1234567@188.170.176.190:8025 /Streaming/Channels/101?transportmode=unicast&profile=Profile_1"]
    await video_stream(websocket, rtsp_url)


@app.post("/getlist")
async def get_list_checked_file(req: Request):
    json_data = await req.json()
    print(json_data)
    return "good"


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
    arch = Path("./archive")
    if not os.path.exists(arch):
        os.makedirs(arch)
        print("Папка успешно создана!")
    else:
        print("Папка уже существует.")
        img = Path("./image")
    if not os.path.exists(img):
        os.makedirs(img)

    file_path = Path(arch, file.filename)
    print(file_path)

    result_list = []

    try:
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        unarchived(file_path)
        try:
            vid = Path("./video")
            if not os.path.exists(vid):
                os.makedirs(vid)

            list_dir = os.listdir(vid)

        except Exception as e:
            return {"directory_video_is_empty": e.args}

        for file in list_dir:
            # print(file)
            url = f"/processed_video/{file}"
            # print(url)
            lbl = Path("./labels")
            if not os.path.exists(lbl):
                os.makedirs(lbl)

            image_dir = os.listdir(os.path.join(img, os.path.splitext(file)[0]))
            labels_dir = os.listdir(os.path.join(lbl, os.path.splitext(file)[0]))
            result_image = []
            img_list = []
            label_list = []

            if len(image_dir) != 0:
                for image, label in zip(image_dir, labels_dir):
                    with open(os.path.join((os.path.join(lbl, os.path.splitext(file)[0])), label), 'r') as file1:
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

                    # result_list.append({"url": url, "image": result_image})
                    img_list.append(result_image)
            else:
                result_image = {
                    "image_name": "no_weapon_detected",
                    "image_url": 0,
                    "class_name": "no_weapon_detected"
                }
                # result_list.append({"url": url, "image": result_image})
                img_list.append(result_image)

            result_list.append({"url": url, "images": img_list})

            print(result_list)

        return json.dumps(result_list)
    except Exception as e:
        return {"message": e.args}


# Создаем новый маршрут для наших статических файлов
static_router = routing.APIRouter(route_class=APIRoute)


@static_router.get("/processed_video/{filename}")
def get_static_file(filename: str):
    vid = Path("./video")
    if not os.path.exists(vid):
        os.makedirs(vid)
        print("Папка успешно создана!")
    else:
        print("Папка уже существует.")

    # Определите путь к файлу на сервере FastAPI
    file_path = os.path.join(vid, filename)
    print(file_path)

    return FileResponse(file_path)


app.include_router(static_router)


@static_router.get("/processed_image/{video_name}/{filename}")
def get_static_image(filename: str, video_name: str):
    img = Path("./image")
    if not os.path.exists(img):
        os.makedirs(img)
        print("Папка успешно создана!")
    else:
        print("Папка уже существует.")

    # Определите путь к файлу на сервере FastAPI
    file_path = os.path.join(os.path.join(video_name), filename)

    return FileResponse(file_path)


app.include_router(static_router)
