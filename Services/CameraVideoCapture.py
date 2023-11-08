import cv2


class RTSPCamera:
    def __init__(self, username, password, rtsp_url):
        """ учетные данные для авторизации """
        self.username = username
        self.password = password
        """ RTSP URL вашей камеры """
        self.rtsp_url = rtsp_url
        self.cap = None

    def connect(self):
        """ Форматирование RTSP URL с учетом username и password """
        rtsp_formatted_url = f"rtsp://{self.username}:{self.password}@{self.rtsp_url}"
        """ Подключение к камере """
        self.cap = cv2.VideoCapture(rtsp_formatted_url)

    def read_frame(self):
        """ Получение кадров из видеопотока """
        if self.cap is not None:
            ret, frame = self.cap.read()
            if ret:
                return frame
        return None

    def disconnect(self):
        if self.cap is not None:
            self.cap.release()
            self.cap = None
        cv2.destroyAllWindows()


# Пример использования класса RTSPCamera
# username = "your_username"
# password = "your_password"
# rtsp_url = "your_rtsp_url"
#
# camera = RTSPCamera(username, password, rtsp_url)
# camera.connect()
#
# while True:
#     frame = camera.read_frame()
#     if frame is not None:
#         """ Здесь добавить обработку видеопотока """
#         cv2.imshow("RTSP Stream", frame)
#     """ Нажмите 'q', чтобы выйти из цикла """
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# camera.disconnect()
