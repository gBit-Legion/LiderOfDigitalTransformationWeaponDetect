FROM python:3.10-slim

WORKDIR /fastAPI

#
COPY ./requirements.txt /fastAPI/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /fastAPI/requirements.txt
#
COPY . /fastAPI

EXPOSE 8000
#
# CMD ["gunicorn",  "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8080", "Application.main:app"]