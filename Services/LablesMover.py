import os
import shutil


class DatasetSpliter:
    def __init__(self, source_folder, destination_folder):
        self.source_folder = source_folder
        self.destination_folder = destination_folder

    def move_files(self, files):
        os.makedirs(os.path.join(self.destination_folder, "images"), exist_ok=True)
        os.makedirs(os.path.join(self.destination_folder, "labels"), exist_ok=True)
        for file in files:
            source_image_path = os.path.join(self.source_folder, 'images', file)
            source_label_path = os.path.join(self.source_folder, "labels",
                                             file.replace(".jpg", ".txt").replace(".jpeg", ".txt").replace(".png",
                                                                                                           ".txt").replace(
                                                 ".webp", ".txt").replace(".JPG", ".txt"))
            destination_image_path = os.path.join(self.destination_folder, "images", file)
            destination_label_path = os.path.join(self.destination_folder, "labels",
                                                  file.replace(".jpg", ".txt").replace(".jpeg", ".txt").replace(".png",
                                                                                                                ".txt").replace(
                                                      ".webp", ".txt").replace(".JPG", ".txt"))
            shutil.move(source_image_path, destination_image_path)
            shutil.move(source_label_path, destination_label_path)
