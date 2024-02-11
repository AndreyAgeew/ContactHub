import csv
from typing import List

from .contact import Contact
from .phonebook_mixins import (
    AddContactMixin,
    DisplayContactsMixin,
    EditContactMixin,
    SearchContactMixin,
)


class PhoneBook(
    AddContactMixin, SearchContactMixin, DisplayContactsMixin, EditContactMixin
):
    """
    Класс телефонного справочника (csv файл) для управления контактами.

    Этот класс интегрирует функциональность различных миксинов для добавления,
    поиска, отображения и редактирования контактов, а также предоставляет методы
    для загрузки и сохранения контактов в CSV-файл.

    Атрибуты:
        filename (str): Путь к файлу CSV, в котором хранятся контакты.
        records (List[Contact]): Список контактов, загруженных из файла.

    Методы:
        load_records: Загружает контакты из CSV-файла.
        save_records: Сохраняет текущие контакты в CSV-файл.
    """

    def __init__(self, filename: str) -> None:
        """
        Инициализирует экземпляр телефонного справочника с заданным именем файла.

        Параметры:
            filename (str): Путь к файлу CSV, в котором хранятся контакты.
        """
        self.filename = filename
        self.records: List[Contact] = self.load_records()

    def load_records(self) -> List[Contact]:
        """
        Загружает записи контактов из CSV файла.

        Возвращает:
            List[Contact]: Список контактов, загруженных из файла.
        """
        records = []
        try:
            with open(self.filename, "r", newline="", encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if row:  # Проверка на пустую строку для исключения пустых записей
                        records.append(Contact(*row))
        except FileNotFoundError:
            open(self.filename, "w").close()  # Создание файла, если он не существует
        return records

    def save_records(self) -> None:
        """
        Сохраняет все текущие записи контактов в CSV файл.

        Сохранение производится в файл, путь к которому указан в атрибуте filename.
        """
        with open(self.filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            for contact in self.records:
                writer.writerow(contact.to_csv())
