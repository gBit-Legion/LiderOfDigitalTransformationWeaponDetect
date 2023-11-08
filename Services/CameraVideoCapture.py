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

    def stream_video(self):
        width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        while True:
            frame = self.read_frame()
            if frame is not None:
                # result = model(frame, save_txt=True, save_crop=True)
                #
                # for result_item in result:
                #     boxes = result_item.boxes.cpu().numpy()
                #
                #     for box in boxes:
                #         r = box.xyxy[0].astype(int)
                #         cls = box.cls[0].astype(int)
                #         if cls == 0:
                #             label = "knife"
                #         if cls == 1:
                #             label = "pistol"
                #         if cls == 2:
                #             label = "gun"
                #         if cls == 3:
                #             label = "shotgun"
                #
                #         box_color = class_colors.get(cls, (255, 255, 255))
                #
                #         (label_width, label_height), _ = cv2.getTextSize(label, class_font, class_font_scale, 1)
                #         text_position = (r[0], r[1] - 3 - label_height)
                #
                #         cv2.rectangle(frame, (r[0], r[1]), (r[2], r[3]), box_color, 2)
                #         cv2.putText(frame, label, text_position, class_font, class_font_scale, box_color, 2)

                center_x = int(width / 2)
                center_y = int(height / 2)

                """ Рисование красной точки в центре кадра """
                cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)

            """ Нажмите 'q', чтобы выйти из цикла """
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

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
