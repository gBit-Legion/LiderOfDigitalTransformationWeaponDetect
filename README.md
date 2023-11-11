# Система видеодетекции вооруженных людей

<p align="center">
  <img src="https://avatars.mds.yandex.net/get-altay/5579175/2a0000017d6eab64658e6cb31041835f463f/XXL" width="300">
</p>

## Описание

Наше решение - это система, построенная на основе нейронной сети, способная определять людей с оружием на данных, поступающих с камер городского видеонаблюдения. В качестве интерфейса взаимодействия пользователя с системой был реализован веб-сервис, который выделяет оружие и любые косвенные признаки, подтверждающие
присутствие вооруженного человека,

## Установка и запуск

### Установка через Docker-коннтейнер



### Установка вручную

#### Настройка виртуального окружения

Перейдите в директорию со скаченным проектом, откройте терминал и введите следующие команды:

```
python -m venv venv
\venv\Scripts\activate
pip install -r requirements.txt
```

#### Настройка веб-интерфейса

В папке _**frontend**_ создайте два файла для подключения клиентской части к серверной:
* _**.env**_
* _**.env.production**_

В этих файлах необходимо прописать IP-адрес серверной части приложения в формате:
```
VUE_APP_USER_IP_WITH_PORT = *Ваш_IP_адрес*:8080
```

Откройте терминал в папке _**frontend**_, выполните команды:

#### Запуск

В корневой директории проекта в терминале введите команду:

```
uvicorn Application.main:app --host=*IP_адрес_хоста* --port=8000
```

## Поддерживаемые функции

* Реализован механизм загрузки архива видеозаписей для тестирования.
* Загрузка файла с набором RTSP-ссылок доступных камер.
* Реализован механизм определения наличия у человека оружия по видео трансляции с городских камер видеонаблюдения.
* Формирование набора стоп-кадров с выделением объекта интереса и типа оружия.
* Cистемами оповещения по средствам Telegram API с указанием адреса места, где было обнаружено вооруженное лицо.
* Предусмотрен режим дополнительного обучения, чтобы оператор мог после визуального осмотра стоп-кадра дать оценку правильному или ложному срабатыванию системы.
