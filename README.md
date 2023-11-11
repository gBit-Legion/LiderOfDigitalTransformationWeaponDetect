# Система видеодетекции вооруженных людей

<p align="center">
  <img src="https://avatars.mds.yandex.net/get-altay/5579175/2a0000017d6eab64658e6cb31041835f463f/XXL" width="300">
</p>

## Описание

Наше решение - это система, построенная на основе нейронной сети, способная определять людей с оружием на данных, поступающих с камер городского видеонаблюдения. В качестве интерфейса взаимодействия пользователя с системой был реализован веб-сервис, который выделяет оружие и любые косвенные признаки, подтверждающие
присутствие вооруженного человека,

## ⚙️ Установка и запуск


### 🐳 Установка через Docker-контейнер

[ ... ]

### 👷🏿‍♂️ Установка вручную

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
```
npm install
npm run serve
```

#### 🚀 Запуск

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

## Особенности

* **Был собран датасет, который содержит **40.521** экземпляра фотографий вооруженных лиц**

| ![image](https://github.com/gBit-Legion/LiderOfDigitalTransformationWeaponDetect/assets/91145499/a411de26-6219-41d7-8fb9-af9243f7c979) | 
| ----------- |

* **Матрица распределения ошибок**

| ![image](https://github.com/gBit-Legion/LiderOfDigitalTransformationWeaponDetect/assets/91145499/a3ab4589-0091-4b84-ab56-423cf30b1f8c) | 
| ----------- |

* **Графики обучения**

| ![image](https://github.com/gBit-Legion/LiderOfDigitalTransformationWeaponDetect/assets/91145499/475bd172-0bf6-4c88-98ba-9020f66c6483) | ![image](https://github.com/gBit-Legion/LiderOfDigitalTransformationWeaponDetect/assets/91145499/4c69c352-f883-42f3-9b4e-19f5e3f50acf) |
| ----------- | ----------- |

## 📄 Документация

[ ... ]

## 📷 Скринкаст

### 💻 Веб-страница

| ![image](https://github.com/gBit-Legion/LiderOfDigitalTransformationWeaponDetect/assets/91145499/974237c0-f811-4613-87c2-3f7248134381) |
| ![image](https://github.com/gBit-Legion/LiderOfDigitalTransformationWeaponDetect/assets/91145499/ccc22320-1944-457c-97c6-94b782bcf048) | ![image](https://github.com/gBit-Legion/LiderOfDigitalTransformationWeaponDetect/assets/91145499/ffc00bb9-9282-4e15-9a14-292378782454) |
| ----------- | ----------- | ----------- |
| ![image](https://github.com/gBit-Legion/LiderOfDigitalTransformationWeaponDetect/assets/91145499/f4dbef9a-0733-493e-9bd9-3317ec506b3b) | ![image](https://github.com/gBit-Legion/LiderOfDigitalTransformationWeaponDetect/assets/91145499/83fead27-3afa-4a9e-a639-17b35b6906f1) | |

### 📣 Система оповещения Telegram Bot

| ![image](https://github.com/gBit-Legion/LiderOfDigitalTransformationWeaponDetect/assets/91145499/5f17286a-b5c4-4de7-b397-c90c1811f70f) | ![image](https://github.com/gBit-Legion/LiderOfDigitalTransformationWeaponDetect/assets/91145499/eeca1fae-98f7-47b9-962e-883f46dd3d00) | ![image](https://github.com/gBit-Legion/LiderOfDigitalTransformationWeaponDetect/assets/91145499/60ee9093-846d-44c3-8990-7c91d0704064) | ![image](https://github.com/gBit-Legion/LiderOfDigitalTransformationWeaponDetect/assets/91145499/e0fda414-bb71-4723-b3d8-e6a64e945451) |
| ----------- | ----------- | ----------- | ----------- |
