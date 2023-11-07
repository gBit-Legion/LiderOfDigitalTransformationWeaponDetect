import os

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import File, UploadFile
from pathlib import Path
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
    if not os.path.exists("../upload"):
        os.makedirs("../upload")
        print("Папка успешно создана!")
    else:
        print("Папка уже существует.")
    print(file.filename)
    file_path = Path("../upload", str({file.filename}))
    try:
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        return {"message": "File saved successfully"}

    except Exception as e:
        return {"message": e.args}


@app.post("/archive")
async def archive_upload():
    pass
