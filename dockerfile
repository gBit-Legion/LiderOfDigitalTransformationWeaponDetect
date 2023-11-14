
# FROM dongsky/pytorch-gpu:latest
FROM python:3.9.18-slim-bullseye
WORKDIR .

#
COPY ./requirements.txt ./requirements.txt

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
    RUN apt-get install ubuntu-restricted-extras -y
#
COPY . .

EXPOSE 8000
#
# CMD ["gunicorn",  "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8080", "Application.main:app"]
