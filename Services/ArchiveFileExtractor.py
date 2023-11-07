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