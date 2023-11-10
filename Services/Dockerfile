FROM python:3.10
WORKDIR /telegrambot
COPY requirements_for_bot.txt .
RUN pip install --no-cache-dir -r requirements_for_bot.txt
COPY TgBotKeeper.py TgBotKeeper.py
CMD python TgBotKeeper.py