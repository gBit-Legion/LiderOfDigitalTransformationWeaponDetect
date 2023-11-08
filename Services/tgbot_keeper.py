import telebot
import threading
from telebot import types
from loguru import logger



TOKEN = '6686505205:AAHhdgG7ZZ7Dmq3ziVXMGzn5gHPi58IJM9s'
bot = telebot.TeleBot(TOKEN)
logger.success('telega is started')

# Словарь для хранения данных о трансляции местоположения для каждого чата
location_transmissions = {}


def stop_location_transmission(chat_id):
    if chat_id in location_transmissions:
        # Остановка трансляции местоположения
        location_transmissions.pop(chat_id)
        print(f"Трансляция местоположения для чата {chat_id} завершена. Спасибо!")
    else:
        print(f"Трансляция местоположения для чата {chat_id} не активна.")


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button = types.KeyboardButton(text="Запустить трансляцию местоположения 📍", request_location=True)
    markup.add(button)
    bot.send_message(chat_id,
                     "Привет! Я могу транслировать ваше местоположение в реальном времени. Нажмите кнопку ниже, чтобы начать.",
                     reply_markup=markup)


@bot.message_handler(func=lambda message: True, content_types=['location'])
def handle_location(message):
    chat_id = message.chat.id
    latitude = message.location.latitude
    longitude = message.location.longitude

    if chat_id in location_transmissions:
        # Обновление уже существующей трансляции местоположения
        location_transmissions[chat_id] = (latitude, longitude)
    else:
        # Создание новой трансляции местоположения
        location_transmissions[chat_id] = (latitude, longitude)

        # Запуск таймера на завершение трансляции через 8 часов
        threading.Timer(28800, stop_location_transmission, args=[chat_id]).start()

    # Вывод текущих координат в консоль
    print(f"Текущее местоположение для чата {chat_id}: Широта: {latitude}, Долгота: {longitude}")

    # Запуск таймера на обновление местоположения каждые 10 секунд
    threading.Timer(10, update_location, args=[chat_id]).start()


def update_location(chat_id):
    if chat_id in location_transmissions:
        # Получение текущего местоположения из словаря
        latitude, longitude = location_transmissions[chat_id]

        # Вывод обновленных координат в консоль
        print(f"Обновленное местоположение для чата {chat_id}: Широта: {latitude}, Долгота: {longitude}")

        # Запуск таймера на следующее обновление местоположения
        threading.Timer(10, update_location, args=[chat_id]).start()


bot.polling()