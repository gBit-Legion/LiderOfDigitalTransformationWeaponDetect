import asyncio
import json

import os

import cv2
import numpy as np
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request, routing
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


@app.get("/static/{filename}")
async def return_html_file(filename: str):
    return FileResponse(f"./Frontend/yolo/{filename}")


stop_stream = False


@app.get("/stop_stream")
async def stop_stream_endpoint():
    global stop_stream
    stop_stream = True
    return {"message": "Stream stopped"}


@app.get("/serve/{camera_id}")
async def serve_video(camera_id: int):
    url = ['rtsp://admin:A1234567@188.170.176.190:8025  /Streaming/Channels/101?transportmode=unicast&profile=Profile_1']
    video_processor = RTSPCamera(url, "./labels", "./image")
    global stop_stream
    stop_stream = False

    async def generate_frames():
        while not stop_stream:
            for frame in video_processor.process_videos():
                frame_np = np.array(next(frame)).astype(np.uint8)

                _, jpg_frame = cv2.imencode(".jpg", frame_np)
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + jpg_frame.tobytes() + b'\r\n')
    return StreamingResponse(generate_frames(), media_type='multipart/x-mixed-replace; boundary=frame')


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
    if not os.path.exists("./archive"):
        os.makedirs("./archive")
        print("Папка успешно создана!")
    else:
        print("Папка уже существует.")
    if not os.path.exists("./image"):
        os.makedirs("./image")

    file_path = Path("./archive", file.filename)
    print(file_path)

    result_list = []

    try:
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        unarchived(file_path)
        try:
            list_dir = os.listdir("./video")

        except Exception as e:
            return {"directory_video_is_empty": e.args}

        for file in list_dir:
            # print(file)
            url = f"/processed_video/{file}"
            # print(url)
            image_dir = os.listdir(f"./image/{os.path.splitext(file)[0]}")
            labels_dir = os.listdir(f"./labels/{os.path.splitext(file)[0]}")
            result_image = []
            img_list = []
            label_list = []

            if len(image_dir) != 0:
                for image, label in zip(image_dir, labels_dir):
                    with open(f'./labels/{os.path.splitext(file)[0]}/{label}', 'r') as file1:
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
    if not os.path.exists("./video"):
        os.makedirs("./video")
        print("Папка успешно создана!")
    else:
        print("Папка уже существует.")

    # Определите путь к файлу на сервере FastAPI
    file_path = "./video/" + filename
    print(file_path)

    return FileResponse(file_path)


app.include_router(static_router)


@static_router.get("/processed_image/{video_name}/{filename}")
def get_static_image(filename: str, video_name: str):
    if not os.path.exists("./image"):
        os.makedirs("./image")
        print("Папка успешно создана!")
    else:
        print("Папка уже существует.")

    # Определите путь к файлу на сервере FastAPI
    file_path = f"./image/{video_name}/" + filename

    return FileResponse(file_path)


app.include_router(static_router)
