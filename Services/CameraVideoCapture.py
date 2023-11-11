import numpy as np

from Services.yolo_connet import *
import concurrent.futures

import os


class RTSPCamera:
    def __init__(self, rtsp_links, save_labels_folder, save_frames_folder):
        self.rtsp_links = rtsp_links
        self.save_labels_folder = save_labels_folder
        self.save_frames_folder = save_frames_folder

    def process_videos(self):
        if not os.path.exists(self.save_frames_folder):
            os.makedirs(self.save_frames_folder)
        if not os.path.exists(self.save_labels_folder):
            os.makedirs(self.save_labels_folder)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for index, rtsp_link in enumerate(self.rtsp_links):
                save_frames_folder = os.path.join(self.save_frames_folder, f'camera_{index + 1}')
                save_labels_folder = os.path.join(self.save_labels_folder, f'camera_{index + 1}')
                futures.append(executor.submit(self.process_video, rtsp_link, index, save_frames_folder,
                                               save_labels_folder))

            for future in concurrent.futures.as_completed(futures):
                try:
                    yield future.result()
                except Exception as e:
                    print(f"Error processing video: {e}")

    def process_video(self, rtsp_link, index, save_frames_folder, save_labels_folder):
        capture = cv2.VideoCapture(rtsp_link)
        capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        capture.set(cv2.CAP_PROP_POS_MSEC, 100)

        if not capture.isOpened():
            raise Exception(f'Failed to open RTSP link: {rtsp_link}')

        frame_count = 0

        class_labels = ['knife', 'pistol', 'gun', 'riffle']

        while True:
            ret, frame = capture.read()

            if ret:
                result = model(frame, conf=0.3)

                for result_item in result[0]:
                    boxes = result_item[:, :4].cpu().numpy()
                    classes = result_item[:, 5].cpu().numpy()
                    confidences = result_item[:, 4].cpu().numpy()

                    for box, cls, conf in zip(boxes, classes, confidences):
                        x1, y1, x2, y2 = box.astype(int)
                        cls = int(cls)
                        conf = round(float(conf), 2)

                        label = class_labels[cls] + str(conf)
                        box_color = class_colors.get(cls, (255, 255, 255))

                        (label_width, label_height), _ = cv2.getTextSize(label, class_font, class_font_scale, 1)
                        text_position = (x1, y1 - 3 - label_height)

                        cv2.rectangle(frame, (x1, y1), (x2, y2), box_color, 2)
                        cv2.putText(frame, label, text_position, class_font, class_font_scale, box_color, 2)

                        if frame_count % 30 == 0:
                            save_frame_path = os.path.join(save_frames_folder, f'frame_{frame_count}.jpg')
                            cv2.imwrite(save_frame_path, frame)

                            frame_height, frame_width, _ = frame.shape
                            x_center = (x1 + x2) / 2 / frame_width
                            y_center = (y1 + y2) / 2 / frame_height
                            box_width = (x2 - x1) / frame_width
                            box_height = (y2 - y1) / frame_height

                            txt_file_path = os.path.join(save_labels_folder, f'frame_{frame_count}.txt')
                            with open(txt_file_path, 'w') as txt_file:
                                txt_file.write(f'{cls} {x_center} {y_center} {box_width} {box_height}\n')

                        frame_count += 1

                yield frame

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            else:
                break

        capture.release()
#
# rtsp_links = ['rtsp://admin:A1234567@188.170.176.190:8025/Streaming/Channels/101?transportmode=unicast&profile=Profile_1',
#               'rtsp://26.114.135.146:8554/streaming']
#
# video_processor = RTSPCamera(rtsp_links, "./labels", "./image")
#
# while True:
#     for frame in video_processor.process_videos():
#         frame_np = np.fromstring(frame, np.uint8)
#
#         cv2.imshow("Frame", frame_np)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
# cv2.destroyAllWindows()