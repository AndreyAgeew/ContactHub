from input_helpers import (
    get_name,
    get_organization,
    get_patronymic,
    get_personal_phone,
    get_surname,
    get_work_phone,
)
from validators import (
    validate_name,
    validate_organization,
    validate_personal_phone_number,
    validate_work_phone_number,
)

from .contact import Contact


class ContactManagementMixin:
    """
    Миксин предназначен для управления контактами в телефонном справочнике.

    Этот миксин добавляет возможности для добавления новых контактов, поиска существующих контактов
    по определённым критериям, отображения списка всех контактов, а также редактирования
    информации о контактах.

    Методы:
    - _add_contact: Запрашивает данные у пользователя и добавляет новый контакт.
    - _find_contact: Выводит подменю для поиска контакта по фамилии или личному телефону.
    - __find_contact_by_surname: Ищет и отображает контакты по фамилии.
    - __find_contact_by_personal_number: Ищет и отображает контакт по личному номеру телефона.
    - _edit_contact: Редактирует информацию о контакте после поиска по личному номеру телефона.
    """

    def _add_contact(self) -> None:
        """
        Запрашивает у пользователя данные для создания нового контакта и добавляет его в справочник.
        Для каждого поля контакта выполняется соответствующая валидация введённых данных.
        После успешного создания контакта, информация сохраняется в справочник.
        """
        # Пример кода для запроса данных у пользователя и валидации
        surname = get_surname()
        name = get_name()
        patronymic = get_patronymic()
        organization = get_organization()
        work_phone = get_work_phone()
        personal_phone = get_personal_phone(self.phonebook.records)

        contact = Contact(
            surname, name, patronymic, organization, work_phone, personal_phone
        )
        self.phonebook.add_contact(contact)
        self.phonebook.save_records()
        print("Контакт успешно добавлен.")

    def _find_contact(self) -> None:
        """
        Отображает пользователю подменю для выбора способа поиска контактов:
        - По фамилии.
        - По личному номеру телефона.
        Пользователь может отменить операцию и вернуться в главное меню.
        """

    def __find_contact_by_surname(self) -> None:
        """
        Запрашивает у пользователя фамилию и отображает все контакты с соответствующей фамилией.
        Если контакты не найдены, выводится соответствующее сообщение.
        """

    def __find_contact_by_personal_number(self) -> None:
        """
        Запрашивает у пользователя личный номер телефона и отображает контакт с этим номером.
        Если контакт не найден, выводится сообщение о том, что контакты не найдены.
        """

    def _edit_contact(self) -> None:
        """
        Позволяет пользователю редактировать контакт.
        Пользователь вводит личный номер телефона для поиска контакта.
        Если контакт найден, пользователь может ввести новые данные для его полей.
        Для каждого поля предусмотрена валидация введённых данных.
        После завершения редактирования, обновлённая информация сохраняется в справочник.
        """
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
            new_surname = get_surname()

        new_name = input(f"Новое имя (текущее: {contact.name}): ")
        if new_name and not validate_name(new_name):
            print("Неверный формат имени.")
            new_name = get_name()

        new_patronymic = input(f"Новое отчество (текущее: {contact.patronymic}): ")
        if new_patronymic and not validate_name(new_patronymic):
            print("Неверный формат отчества.")
            new_patronymic = get_patronymic()

        new_organization = input(
            f"Новая организация (текущая: {contact.organization}): "
        )
        if new_organization and not validate_organization(new_organization):
            print("Неверный формат названия организации.")
            new_organization = get_organization()

        new_work_phone = input(
            f"Новый рабочий телефон (текущий: {contact.work_phone}): "
        )
        if new_work_phone and not validate_work_phone_number(new_work_phone):
            print("Неверный формат рабочего телефона.")
            new_work_phone = get_work_phone()

        while True:
            new_personal_phone = input(
                f"Новый личный телефон (текущий: {contact.personal_phone}): "
            )
            if new_personal_phone and not validate_personal_phone_number(
                new_personal_phone, records=self.phonebook.records
            ):
                print("Неверный формат личного телефона.")
            else:
                break

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
