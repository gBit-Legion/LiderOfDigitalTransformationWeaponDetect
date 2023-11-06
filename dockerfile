FROM python:3.9-slim

WORKDIR /fastAPI

#
COPY ./requirements.txt /fastAPI/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /fastAPI/requirements.txt
#
COPY . /fastAPI

#
# CMD ["gunicorn",  "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8080", "Application.main:app"]