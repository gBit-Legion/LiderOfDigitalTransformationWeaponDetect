from Services.yolo_connet import *
import os

class RTSPCamera:
    def __init__(self, rtsp_links, save_labels_folder, save_frames_folder):
        self.rtsp_links = rtsp_links
        self.save_labels_folder = save_labels_folder
        self.save_frames_folder = save_frames_folder

    def process_video(self):
        capture = cv2.VideoCapture(self.rtsp_links[0])
        capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        capture.set(cv2.CAP_PROP_POS_MSEC, 100)

        if not capture.isOpened():
            print(self.rtsp_links[0])
            raise Exception(f'Failed to open RTSP link: {self.rtsp_links[0]}')

        frame_count = 0
        class_labels = ['knife', 'pistol', 'gun', 'riffle']

        while True:

            ret, frame = capture.read()

            if ret:

                if torch.cuda.is_available():
                    result = model(frame, device=0)
                else:
                    result = model(frame, conf=0.3)

                result = model(frame, conf=0.3)

                for result_item in result[0]:
                    print(result_item)
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
                            save_frame_path = os.path.join(self.save_frames_folder, f'frame_{frame_count}.jpg')
                            cv2.imwrite(save_frame_path, frame)

                            frame_height, frame_width, _ = frame.shape
                            x_center = (x1 + x2) / 2 / frame_width
                            y_center = (y1 + y2) / 2 / frame_height
                            box_width = (x2 - x1) / frame_width
                            box_height = (y2 - y1) / frame_height

                            txt_file_path = os.path.join(self.save_labels_folder, f'frame_{frame_count}.txt')
                            with open(txt_file_path, 'w') as txt_file:
                                txt_file.write(f'{cls} {x_center} {y_center} {box_width} {box_height}\n')

                        frame_count += 1

                    cv2.imshow("Cam", frame)

                _, jpeg = cv2.imencode('.jpg', frame)
                frame_bytes = jpeg.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n\r\n')

