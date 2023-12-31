''' Код для разделения сохраниения и разделения обучающей выборки '''
import os
import shutil
from pathlib import Path

from Services.ArchiveFileExtractor import ZipFileExtractor
from Services.TableParser import *
from Services.YoloHandlers import VideoProcessor


def dataset_spliter(archive_path):
    ''' Путь к архиву с лейблами '''
    lables_zip_file_path = archive_path
    ''' Путь куда нужно переместить лейблы из архива '''
    train_dataset_dir = os.path.join('./dataset/train/labels')

    ''' Пути для хранения обучающей и тестовой выборок '''
    source_dir = os.path.join('./dataset/train')
    val_dir = os.path.join("./dataset/val")

    ''' Извлечение лейблов из архива '''
    zip_extractor = ZipFileExtractor(lables_zip_file_path)
    zip_extractor.extract_files(train_dataset_dir)


# ''' Разделение датасета на обучающую и тестовую выборки '''
# image_files = [f for f in os.listdir(source_dir + os.path.join('/images'))]
# image_files_train, image_files_val = train_test_split(image_files, test_size=0.15, random_state=42)
#
# spliter = DatasetSpliter(source_dir, val_dir)
# spliter.move_files(image_files_val)
''' ------------------------------------------------------------- '''

''' Код для получения видеофайлов из архива и их обработки '''


def delete_tree(folder):
    for filename in os.listdir(folder):
        file_path = folder + "/" + filename
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def unarchived(file_name):
    zip_file_path = file_name

    delete_tree("./labels")
    delete_tree("./video")
    delete_tree("./image")

    extract_dir = "./archive"
    print(extract_dir)
    print(3)

    """ Создаем экземпляр класса ZipFileExtractor """
    zip_extractor = ZipFileExtractor(zip_file_path)

    """ Разархивируем файлы в указанный каталог """
    zip_extractor.extract_files(extract_dir)

    ''' Создание экземпляра VideoProcessor и обработка видео в указанной папке '''

    input_folder = './archive'
    output_folder = './video'

    processor = VideoProcessor(input_folder, output_folder, "./image", "./labels")
    processor.process_videos()
    if len(os.listdir("./archive")) != 0:
        for filename in os.listdir("./archive"):

            file_path = "./archive/" + filename
            # Проверяем, является ли объект файлом
            if os.path.isfile(file_path):
                # Удаляем файл
                os.remove(file_path)


''' ------------------------------------------------------ '''


# Пример использования
def excel_parser(file_path):
    table_parser = TableParser()
    parsed_data = table_parser.parse_xlsx_file()
