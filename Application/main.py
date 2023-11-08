import json
import os

from fastapi import FastAPI, Form, routing
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import File, UploadFile
from pathlib import Path

from fastapi.routing import APIRoute

app = FastAPI()

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

    print(file.filename)

    file_path = Path("./archive", file.filename)
    result_list = []

    print(file_path)
    try:
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        list_dir = os.listdir("./video")
        for file in list_dir:
            url = f"url: /processed_video/{file}"
            result_list.append({"url": url})

        return JSONResponse(status_code=200, content=result_list)
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


# Регистрируем новый роутер в приложении FastAPI
app.include_router(static_router)
