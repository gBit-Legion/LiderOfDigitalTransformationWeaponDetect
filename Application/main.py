import glob
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
# from Services.TgBotKeeper import *

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


# Запуск процесса для обработки файла
# p = Process(target=bot_start)
# p.start()
# p.join()

@app.get("/static/{filename}")
async def return_html_file(filename: str):
    return FileResponse(f"./Frontend/yolo/{filename}")


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
            print(file)
            url = f"/processed_video/{file}"
            print(url)
            # print(os.listdir(os.path.join("./image", os.path.splitext(file)[0])))
            # image_dir = os.listdir(f"../image/{os.path.splitext(file)[0]}")
            #
            # print(os.listdir(os.path.join(f"./image,{os.path.splitext(file)[0]}")))
            image_dirs = f"./image/{os.path.splitext(file)[0]}"
            print(image_dirs)
            image_dir = glob.glob(f"{image_dirs}/*.*")
            # with os.scandir(image_dirs) as entries:
            #     for entry in entries:
            #         if entry.is_file():
            #             image_dir = entry.name
            # print(image_dir)
            if len(image_dir) != 0:

                for image in image_dir:
                    result_image = {"image_name": os.path.splitext(image)[0],
                                    "image_url": f"/processed_image/{os.path.splitext(file)[0]}/{image}",
                                    "class_name": "riffle"
                                    }
                    result_list.append({"url": url, "image": result_image})
            else:
                result_image = {
                    "image_name": "no_weapon_detected",
                    "image_url": 0,
                    "class_name": "no_weapon_detected"
                 }
                result_list.append({"url": url, "image": result_image})
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
