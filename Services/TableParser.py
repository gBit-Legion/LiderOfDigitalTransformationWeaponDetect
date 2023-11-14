import openpyxl


class TableParser:
    def __init__(self, file_path):
        """ Путь к файлу .xlsx """
        self.file_path = file_path
        """ Общий список для хранения данных """
        self.data = []

    def parse_xlsx_file(self):
        """ Открываем таблицу """
        workbook = openpyxl.load_workbook(self.file_path)
        """ Выбираем активный лист """
        sheet = workbook.active
        """ Указатель на начало таблицы """
        rows = sheet.iter_rows(values_only=True)
        # """ Пропускаем первую строку """
        # next(rows)
        """ Собираем данные со строк """
        for row in rows:
            self.data.append(list(row))
        return self.data



