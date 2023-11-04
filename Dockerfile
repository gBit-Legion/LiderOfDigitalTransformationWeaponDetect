
# official python image(use your python version, but check this in docker documntation)
# подключаем образ питона, посмотрите какие есть на официальном сайте
FROM python:3.9

# set enviroment variables
# устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set current directory for work
# устанавливаем рабочий каталог
WORKDIR /fastApiProject

# copy file requirements.txt to workdir
# Копируем файл зависимостей в рабочую директорию внутри контейнера
COPY ./requirements.txt /fastApiProject/requirements.txt

# Run pip and install requiremnts withous localy saved
# Устанавливаем зависимости и не сохраняем их локально
RUN pip install --no-cache-dir --upgrade -r /fastApiProject/requirements.txt

# Copy project file to work directory
# Копируем файлы для работы

COPY ./Application /fastApiProject/Application
COPY ./Database /fastApiProject/Database
COPY ./ML_AI_NN /fastApiProject/ML_AI_NN
COPY ./Frontend /fastApiProject/Frontend

# Run
# Запускаем проект
CMD ["gunicorn",
     "-k",
     "Application.main:app",
     "--workers",
     "4",
     "--worker-class",
     "uvicorn.workers.UvicornWorker",
     "--bind",
     "0.0.0.0:8080"]