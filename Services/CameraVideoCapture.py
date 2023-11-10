import cv2
import concurrent.futures
from ultralytics import YOLO
import os

model = YOLO("./best.pt")
class_colors = \
    {
        0: (255, 0, 0),
        1: (0, 255, 0),
        2: (0, 0, 255),
        3: (255, 255, 0)
    }

class_font = cv2.FONT_HERSHEY_SIMPLEX
class_font_scale = 1.2

class RTSPCamera:
    def __init__(self, rtsp_links):
        self.rtsp_links = rtsp_links
        self.window_names = [f'Video Stream {index}' for index in range(len(rtsp_links))]

    def process_videos(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for index, rtsp_link in enumerate(self.rtsp_links):
                futures.append(executor.submit(self.process_video, rtsp_link, index))

            for _ in concurrent.futures.as_completed(futures):
                pass

    def process_video(self, rtsp_link, index):
        capture = cv2.VideoCapture(rtsp_link)

        if not capture.isOpened():
            raise Exception(f'Failed to open RTSP link: {rtsp_link}')

        window_name = self.window_names[index]
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

        class_labels = ['knife', 'pistol', 'gun', 'riffle']

        while capture.isOpened():
            ret, frame = capture.read()

            if ret:
                result = model(frame, conf=0.3)

                for result_item in result:
                    boxes = result_item.boxes.cpu().numpy()

                    for box in boxes:
                        r = box.xyxy[0].astype(int)
                        cls = box.cls[0].astype(int)

                        conf = round(box.conf[0].astype(float), 2)

                        label = class_labels[cls] + str(conf)
                        box_color = class_colors.get(cls, (255, 255, 255))

                        (label_width, label_height), _ = cv2.getTextSize(label, class_font, class_font_scale, 1)
                        text_position = (r[0], r[1] - 3 - label_height)

                        cv2.rectangle(frame, (r[0], r[1]), (r[2], r[3]), box_color, 2)
                        cv2.putText(frame, label, text_position, class_font, class_font_scale, box_color, 2)

                yield frame

                cv2.imshow(window_name, frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        capture.release()
        cv2.destroyWindow(window_name)

rtsp_links = ['rtsp://admin:A1234567@188.170.176.190:8031/Streaming/Channels/101?transportmode=unicast&profile=Profile_1',
              'rtsp://26.114.135.146:8554/streaming']

rtsp_camera = RTSPCamera(rtsp_links)

for frame in rtsp_camera.process_videos():
    # Обрабатывай фреймы здесь #
    pass
