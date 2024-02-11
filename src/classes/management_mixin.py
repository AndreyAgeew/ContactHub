from input_helpers import (
    get_name,
    get_organization,
    get_patronymic,
    get_personal_phone,
    get_surname,
    get_work_phone,
)
from validators import validate_name, validate_organization, validate_phone_number

from .contact import Contact


class ContactManagementMixin:
    def _add_contact(self):
        """Запрашивает у пользователя данные и добавляет новый контакт в телефонную книгу."""
        surname = get_surname()
        name = get_name()
        patronymic = get_patronymic()
        organization = get_organization()
        work_phone = get_work_phone()
        personal_phone = get_personal_phone()

        contact = Contact(
            surname, name, patronymic, organization, work_phone, personal_phone
        )
        self.phonebook.add_contact(contact)
        self.phonebook.save_records()
        print("Контакт добавлен.")

    def _find_contact(self):
        """Подменю для поиска контака по фамилии или личному телефону и отображает найденные контакты."""
        while True:
            print("\n1. По фамилии")
            print("2. По личному телефону")
            print("3. Отмена\n")
            choice = input("Выберите действие: ")
            if choice == "1":
                self.__find_contact_by_surname()
            elif choice == "2":
                self.__find_contact_by_personal_number()
            elif choice == "3":
                break
            else:
                print("Некорректный выбор. Пожалуйста, введите число от 1 до 3.")

    def __find_contact_by_surname(self):
        """Запрашивает у пользователя фамилию и отображает найденные контакты."""
        surname = input("Введите фамилию для поиска: ")
        found_contacts = self.phonebook.search_contact_by_surname(surname)
        if found_contacts:
            for contact in found_contacts:
                print(
                    f"{contact.surname}, {contact.name}, {contact.organization}, {contact.work_phone}, {contact.personal_phone}"
                )
        else:
            print("Контакты не найдены.")

    def __find_contact_by_personal_number(self):
        """Запрашивает у пользователя личный телефон и отображает найденный контакт."""
        personal_phone = input("Введите личный телефон для поиска: ")
        found_contact = self.phonebook.search_contact_by_personal_phone(personal_phone)[
            1
        ]
        if found_contact:
            print(
                f"{found_contact.surname}, {found_contact.name}, {found_contact.organization}, {found_contact.work_phone}, {found_contact.personal_phone}"
            )
        else:
            print("Контакты не найдены.")

    def _edit_contact(self):
        """Запрашивает у пользователя информацию для поиска и редактирования контакта."""
        personal_phone = input("Введите личный номер телефона контакта для поиска: ")
        index, contact = self.phonebook.search_contact_by_personal_phone(personal_phone)

        if contact is None:
            print("Контакт не найден.")
            return

            # Запрос подтверждения у пользователя
        print(
            f"Найден контакт: {contact.surname}, {contact.name}, {contact.organization}, {contact.work_phone}, {contact.personal_phone}"
        )
        confirm = input("Вы уверены, что хотите редактировать этот контакт? (да/нет): ")

        if confirm.lower() != "да":
            print("Редактирование отменено.")
            return

        print(
            "Введите новые данные для контакта (оставьте поле пустым, если не хотите его изменять):"
        )

        new_surname = input(f"Новая фамилия (текущая: {contact.surname}): ")
        if new_surname and not validate_name(new_surname):
            print("Неверный формат фамилии.")
            return

        new_name = input(f"Новое имя (текущее: {contact.name}): ")
        if new_name and not validate_name(new_name):
            print("Неверный формат имени.")
            return

        new_patronymic = input(f"Новое отчество (текущее: {contact.patronymic}): ")
        if new_patronymic and not validate_name(new_patronymic):
            print("Неверный формат отчества.")
            return

        new_organization = input(
            f"Новая организация (текущая: {contact.organization}): "
        )
        if new_organization and not validate_organization(new_organization):
            print("Неверный формат названия организации.")
            return

        new_work_phone = input(
            f"Новый рабочий телефон (текущий: {contact.work_phone}): "
        )
        if new_work_phone and not validate_phone_number(new_work_phone):
            print("Неверный формат рабочего телефона.")
            return

        new_personal_phone = input(
            f"Новый личный телефон (текущий: {contact.personal_phone}): "
        )
        if new_personal_phone and not validate_phone_number(new_personal_phone):
            print("Неверный формат личного телефона.")
            return

        # Применение обновленных данных, сохраняя исходные значения для полей, которые не были изменены
        updated_contact = Contact(
            new_surname or contact.surname,
            new_name or contact.name,
            new_patronymic or contact.patronymic,
            new_organization or contact.organization,
            new_work_phone or contact.work_phone,
            new_personal_phone or contact.personal_phone,
        )
        self.phonebook.records[index] = updated_contact
        self.phonebook.save_records()
        print("Контакт успешно обновлен.")
