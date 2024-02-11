from typing import List, Optional, Tuple

from .contact import Contact


class AddContactMixin:
    """
    Миксин для добавления контакта в телефонный справочник.

    Этот миксин предоставляет метод для добавления нового контакта в список
    контактов телефонного справочника.
    """

    def add_contact(self, contact: Contact) -> None:
        """
        Добавляет новый контакт в список контактов.

        Параметры:
            contact (Contact): Экземпляр контакта для добавления.
        """
        self.records.append(contact)


class SearchContactMixin:
    """
    Миксин для поиска контактов по различным критериям.

    Предоставляет методы для поиска контактов по фамилии и личному номеру телефона.
    """

    def search_contact_by_surname(self, surname: str) -> List[Contact]:
        """
        Возвращает список контактов, фамилия которых соответствует заданному запросу.

        Параметры:
            surname (str): Фамилия для поиска контактов.

        Возвращает:
            List[Contact]: Список контактов, удовлетворяющих критерию поиска.
        """
        return [
            contact
            for contact in self.records
            if surname.lower() == contact.surname.lower()
        ]

    def search_contact_by_personal_phone(
        self, personal_phone: str
    ) -> Optional[Tuple[int, Contact]]:
        """
        Возвращает контакт и его индекс по личному номеру телефона.

        Параметры:
            personal_phone (str): Личный номер телефона для поиска.

        Возвращает:
            Tuple[int, Contact] или None: Кортеж, содержащий индекс контакта и сам контакт,
            если контакт найден; иначе None.
        """
        for index, contact in enumerate(self.records):
            if contact.personal_phone == personal_phone:
                return index, contact
        return None, None


class DisplayContactsMixin:
    """
    Миксин для отображения списка контактов.

    Предоставляет метод для вывода информации о всех контактах в телефонном справочнике.
    """

    def display_contacts(self) -> None:
        """
        Выводит информацию о всех контактах в консоль.
        """
        for contact in self.records:
            print(
                f"{contact.surname}, {contact.name}, {contact.patronymic}, "
                f"{contact.organization}, {contact.work_phone}, {contact.personal_phone}"
            )


class EditContactMixin:
    """
    Миксин для редактирования записей в телефонном справочнике.

    Позволяет изменять атрибуты существующего контакта по его идентификатору.
    """

    def edit_contact(self, contact_id: int, **kwargs) -> bool:
        """
        Редактирует атрибуты контакта по его ID.

        Параметры:
            contact_id (int): Идентификатор контакта для редактирования.
            **kwargs: Атрибуты контакта и их новые значения.

        Возвращает:
            bool: True, если редактирование прошло успешно; иначе False.
        """
        if contact_id < 0 or contact_id >= len(self.records):
            print("Контакт с таким ID не найден.")
            return False

        contact = self.records[contact_id]
        for field, value in kwargs.items():
            if hasattr(contact, field):
                setattr(contact, field, value)
            else:
                print(f"Поле '{field}' не существует у контакта.")
                return False

        # Предполагается, что метод save_records() определен в другом месте
        self.save_records()  # Сохраняем изменения в файл
        print("Контакт успешно обновлен.")
        return True
