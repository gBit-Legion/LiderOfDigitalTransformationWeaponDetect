''' Код для разделения сохраниения и разделения обучающей выборки '''
from ArchiveFileExtractor import ZipFileExtractor
from LablesMover import DatasetSpliter
import os

from sklearn.model_selection import train_test_split

''' Путь к архиву с лейблами '''
lables_zip_file_path = 'C:/Users/mides/Downloads/bboxes_yolo.zip'
''' Путь куда нужно переместить лейблы из архива '''
train_dataset_dir = os.path.join('./dataset/train/labels')

''' Пути для хранения обучающей и тестовой выборок '''
source_dir = os.path.join('./dataset/train')
val_dir = os.path.join("./dataset/val")

''' Извлечение лейблов из архива '''
zip_extractor = ZipFileExtractor(lables_zip_file_path)
zip_extractor.extract_files(train_dataset_dir)

''' Разделение датасета на обучающую и тестовую выборки '''
image_files = [f for f in os.listdir(source_dir + os.path.join('/images'))]
image_files_train, image_files_val = train_test_split(image_files, test_size=0.15, random_state=42)

spliter = DatasetSpliter(source_dir, val_dir)
spliter.move_files(image_files_val)
''' ------------------------------------------------------------- '''