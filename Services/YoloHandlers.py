import os
import cv2
import concurrent.futures
from ultralytics import YOLO

model = YOLO('./ML_AI_NN/best.pt')

class_colors = \
    {
        0: (255, 0, 0),
        1: (0, 255, 0),
        2: (0, 0, 255),
        3: (255, 255, 0)
    }

class_font = cv2.FONT_HERSHEY_SIMPLEX
class_font_scale = 1.2


class VideoProcessor:
    def __init__(self, input_folder, output_folder, save_frames_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.save_frames_folder = save_frames_folder

    def process_videos(self):
        ''' Проверка существования выходной папки, иначе создание '''
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        ''' Создание списка всех видеофайлов во входной папке '''
        video_files = [filename for filename in os.listdir(self.input_folder) if filename.endswith('.mp4')]

        ''' Использование ThreadPoolExecutor для многопоточной обработки видео '''
        with concurrent.futures.ThreadPoolExecutor() as executor:
            ''' Запуск обработки каждого видео в отдельном потоке '''
            futures = []
            for self.video_file in video_files:
                input_file = os.path.join(self.input_folder, self.video_file)
                output_file = os.path.join(self.output_folder, f'{self.video_file}')
                save_frames_folder = os.path.join(self.save_frames_folder, f'{os.path.splitext(self.video_file)[0]}')  # Новая папка для сохранения фреймов
                futures.append(executor.submit(self.process_video, input_file, output_file, save_frames_folder))

            ''' Ожидание завершения всех потоков '''
            for future in concurrent.futures.as_completed(futures):
                exception = future.exception()
                if exception:
                    print(f'Ошибка при обработке видео: {exception}')

    def process_video(self, input_file, output_file, save_frames_folder):
        capture = cv2.VideoCapture(input_file)

        ''' Проверка, удалось ли открыть файл '''
        if not capture.isOpened():
            raise Exception(f'Не удалось открыть видеофайл: {input_file}')

        ''' Получение информации о видео '''
        fps = capture.get(cv2.CAP_PROP_FPS)
        width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

        ''' Создание папки для сохранения фреймов '''
        if not os.path.exists(save_frames_folder):
            os.makedirs(save_frames_folder)

        ''' Создание объекта VideoWriter для записи нового видеофайла '''
        fourcc = cv2.VideoWriter_fourcc(*'MP4T')
        out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))
        frame_count = 0

        while capture.isOpened():
            ''' Чтение кадра '''
            ret, frame = capture.read()

            if ret:
                ''' Обработка моделью (Предварительно) '''
                result = model(frame)

                for result_item in result:
                    boxes = result_item.boxes.cpu().numpy()

                    for box in boxes:
                        r = box.xyxy[0].astype(int)
                        cls = box.cls[0].astype(int)
                        if cls == 0:
                            label = "knife"
                        if cls == 1:
                            label = "pistol"
                        if cls == 2:
                            label = "gun"
                        if cls == 3:
                            label = "riffle"

                        box_color = class_colors.get(cls, (255, 255, 255))

                        (label_width, label_height), _ = cv2.getTextSize(label, class_font, class_font_scale, 1)
                        text_position = (r[0], r[1] - 3 - label_height)

                        cv2.rectangle(frame, (r[0], r[1]), (r[2], r[3]), box_color, 2)
                        cv2.putText(frame, label, text_position, class_font, class_font_scale, box_color, 2)

                        if frame_count % 60 == 0:  # Сохранение только каждого 60-го фрейма в папку
                            save_frame_path = os.path.join(save_frames_folder, f'{os.path.splitext(self.video_file)[0]}_frame_{frame_count}.jpg')
                            cv2.imwrite(save_frame_path, frame)

                        frame_count += 1

                # center_x = int(width / 2)
                # center_y = int(height / 2)
                #
                # # Рисование красной точки в центре кадра
                # cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)

                ''' Запись обработанного кадра в новый видеофайл '''
                out.write(frame)

                ''' Прерывание работы по нажатию на клавишу "q" '''
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        # Закрытие видеофайлов
        capture.release()
        out.release()
