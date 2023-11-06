import zipfile

class ZipFileExtractor:
    def __init__(self, zip_file_path):
        self.zip_file_path = zip_file_path

    def extract_files(self, extract_dir):
        """Разархивирует файл в указанный каталог"""
        with zipfile.ZipFile(self.zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)

    def get_file_paths(self):
        """Возвращает список путей ко всем файлам, содержащимся внутри архива"""
        file_paths = []
        with zipfile.ZipFile(self.zip_file_path, 'r') as zip_ref:
            for file_info in zip_ref.infolist():
                file_paths.append(file_info.filename)
        return file_paths


# Пример использования класса ZipFileExtractor
zip_file_path = 'path/to/your/archive.zip'
extract_dir = 'path/to/extract'

""" Создаем экземпляр класса ZipFileExtractor """
zip_extractor = ZipFileExtractor(zip_file_path)

""" Разархивируем файлы в указанный каталог """
zip_extractor.extract_files(extract_dir)

""" Получаем список путей ко всем файлам внутри архива """
file_paths = zip_extractor.get_file_paths()

""" Тут нужно подать их на обработку модели """