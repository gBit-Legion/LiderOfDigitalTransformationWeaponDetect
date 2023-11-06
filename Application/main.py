from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import File, UploadFile

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/file')
async def file_uploader(file: UploadFile):
    #здесь обрабатываем файл
    return {"filename": file.filename}


@app.post("/archive")
async def archive_upload():
    pass
