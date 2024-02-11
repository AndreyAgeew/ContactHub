from typing import List

from .contact import Contact


class AddContactMixin:
    """Миксин для добавления контакта в телефонный справочник."""

    def add_contact(self, contact: Contact) -> None:
        """Добавляет новый контакт в список."""
        self.records.append(contact)


class SearchContactMixin:
    """Миксин для поиска контактов по фамилии."""

    def search_contact_by_surname(self, surname: str) -> List[Contact]:
        """Возвращает список контактов, фамилия которых соответствует запросу."""
        return [
            contact
            for contact in self.records
            if surname.lower() == contact.surname.lower()
        ]

    def search_contact_by_personal_phone(self, personal_phone: str):
        """Возвращает контакт по личному номеру телефона."""
        for index, contact in enumerate(self.records):
            if contact.personal_phone == personal_phone:
                return index, contact
        return None, None


class DisplayContactsMixin:
    """Миксин для отображения контактов."""

    def display_contacts(self) -> None:
        """Выводит информацию о всех контактах."""
        for contact in self.records:
            print(
                f"{contact.surname}, {contact.name}, {contact.patronymic}, {contact.organization}, {contact.work_phone}, {contact.personal_phone}"
            )


class EditContactMixin:
    """
    Миксин для редактирования записей в телефонном справочнике.
    """

    def edit_contact(self, contact_id: int, **kwargs) -> bool:
        """
        Редактирует атрибуты контакта по его ID.
        """
        if contact_id < 0 or contact_id >= len(self.records):
            print("Контакт с таким ID не найден.")
            return False

        contact = self.records[contact_id]
        for field, value in kwargs.items():
            if hasattr(contact, field):
                setattr(contact, field, value)
            else:
                print(f"Поле {field} не существует.")
                return False

        self.save_records()  # Сохраняем изменения в файл
        print("Контакт успешно обновлен.")
        return True
