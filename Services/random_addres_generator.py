from geopy.geocoders import Nominatim
from geopy.distance import distance
from geopy.point import Point
import random


def generate_random_address(center_point, radius):
    geolocator = Nominatim(user_agent="my_app")
    min_lat, min_lon, max_lat, max_lon = generate_boundaries(center_point, radius)

    while True:
        # Генерируем случайные координаты в пределах заданной зоны
        random_lat = random.uniform(min_lat, max_lat)
        random_lon = random.uniform(min_lon, max_lon)

        # Преобразовываем координаты в адрес
        location = geolocator.reverse(Point(random_lat, random_lon))
        if location is not None:
            return location.address, random_lat, random_lon


def generate_boundaries(center_point, radius):
    min_point = distance(kilometers=radius).destination(center_point, 180)  # 180 градусов - южное направление
    max_point = distance(kilometers=radius).destination(center_point, 0)  # 0 градусов - северное направление

    return min_point.latitude, min_point.longitude, max_point.latitude, max_point.longitude


def address_generator():
    center_point = Point(44.8908, 37.3239)  # Центральная точка
    radius = 5
    # Радиус в километрах
    random_address, lat, lon = generate_random_address(center_point, radius)
    return random_address, lat, lon
