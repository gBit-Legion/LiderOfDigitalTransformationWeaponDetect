import json
import os
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Form, routing
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import UploadFile
from pathlib import Path

from fastapi.routing import APIRoute

from Services.CodesForInteraction import *

app = FastAPI()

app.mount("/static", StaticFiles(directory="./Frontend/yolo"), name='static')


@app.get("/static/{filename}")
async def return_html_file(filename: str):
    return FileResponse(f"./Frontend/yolo/{filename}")


origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
        return {"message": "File saved successfully"}

    except Exception as e:
        return {"message": e.args}


@app.post("/archive")
async def archive_upload(file: UploadFile):
    if not os.path.exists("./archive"):
        os.makedirs("./archive")
        print("Папка успешно создана!")
    else:
        print("Папка уже существует.")

    file_path = Path("./archive", file.filename)

    result_list = []
    unarchived()

    try:
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        try:
            list_dir = os.listdir("./video")
        except Exception as e:
            return {"directory_video_is_empty": e.args}

        for file in list_dir:
            url = f"/processed_video/{file}"

            image_dir = os.listdir(f"./image/{os.path.splitext(file)[0]}")
            if len(image_dir) != 0:
                for image in image_dir:
                    result_image = {"image_name": os.path.splitext(image)[0],
                                    "image_url": f"/processed_image/{os.path.splitext(file)[0]}/{image}",
                                    "class_name": "riffle"
                                    }
                    result_list.append({"url": url, "image": result_image})
            else:
                result_image = {"image_name": "no_weapon_detected"}
                result_list.append({"url": url, "image": result_image})
        print(result_list)
        # url_encoded_data = [urllib.parse.quote(json.dumps(item)) for item in result_list]
        # print(url_encoded_data)
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
