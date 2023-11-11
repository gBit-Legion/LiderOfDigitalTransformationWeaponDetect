
FROM python:3.10-slim

WORKDIR .

#
COPY ./requirements.txt ./requirements.txt

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
#
COPY . .

EXPOSE 8000
#
# CMD ["gunicorn",  "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8080", "Application.main:app"]
