import telebot
from geopy.distance import geodesic
from telebot import types
from geopy.geocoders import Nominatim
from loguru import logger



TOKEN = '6817771962:AAFTKHg8UbU7Dy4Hnw0ySMvo9EBRLFBPRuo'
bot = telebot.TeleBot(TOKEN)
logger.success('telega is started')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Отправьте любое фото (имитация отправки изображения с маркированным подозрительным объектом)')

# Обработчик фотографии
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    # Проверяем, что у фотографии есть координаты
    if message.photo[-1].file_id:
        # Получаем координаты фотографии
        photo_latitude = 60.033158  # Заменить на фактические координаты фотографии
        photo_longitude = 30.238523  # Заменить на фактические координаты фотографии

        def get_address(latitude, longitude):
            geolocator = Nominatim(user_agent="location")
            location = geolocator.reverse((latitude, longitude))
            address = location.address
            return address

        latitude = photo_latitude
        longitude = photo_longitude

        address = get_address(latitude, longitude)
        print(address)
        # Отправляем фотографию с координатами
        bot.send_photo(message.chat.id, message.photo[-1].file_id, caption=f'Адрес: {address}') #caption=f'Координаты: {photo_latitude}, {photo_longitude}')


        # Запрашиваем текущее местоположение пользователя

        chat_id = message.chat.id
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        button = types.KeyboardButton(text="Поделиться местоположением 📍", request_location=True)
        markup.add(button)
        bot.send_message(chat_id,"‼️‼️‼️ВНИМАНИЕ‼️‼️‼️ " 
                                 "Был обнаружен подозрительный объект " 
                                 "Отправьте свое местоположение и я рассчитаю расстояние до него.",
                         reply_markup=markup)


        #bot.send_message(message.chat.id, 'Пожалуйста, отправьте ваше текущее местоположение:')
        bot.register_next_step_handler(message, calculate_distance, photo_latitude, photo_longitude)
    else:
        bot.reply_to(message, 'У фото отсутствуют координаты.')

# Обработчик геопозиции пользователя
def calculate_distance(message, photo_latitude, photo_longitude):
    # Получаем координаты пользователя из геопозиции
    user_latitude = message.location.latitude
    user_longitude = message.location.longitude
    # Выводим ник и координаты пользователя в консоль
    print(f'Имя пользователя: {message.chat.username}')
    print(f'Координаты пользователя: {user_latitude}, {user_longitude}')
    # Вычисляем расстояние между координатами
    distance = geodesic((photo_latitude, photo_longitude), (user_latitude, user_longitude)).meters
    rounded_distance = round(distance)
    # Отправляем ответ с расстоянием
    bot.send_message(message.chat.id, f'Расстояние между объектом и вашим местоположением: {rounded_distance} м')

# Прослушивание новых сообщений
bot.polling(none_stop=True)