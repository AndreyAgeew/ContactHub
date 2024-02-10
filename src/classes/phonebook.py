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
    """Основной класс телефонного справочника."""

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.records: List[Contact] = self.load_records()

    def load_records(self) -> List[Contact]:
        """Загружает записи из CSV файла."""
        records = []
        try:
            with open(self.filename, "r", newline="", encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if row:  # Проверка на пустую строку
                        records.append(Contact(*row))
        except FileNotFoundError:
            open(self.filename, "w").close()  # Создать файл, если он не существует
        return records

    def save_records(self) -> None:
        """Сохраняет все текущие записи в CSV файл."""
        with open(self.filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            for contact in self.records:
                writer.writerow(contact.to_csv())
