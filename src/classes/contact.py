from typing import List


class Contact:
    """
    Класс для хранения информации о контакте.

    Атрибуты:
        surname (str): Фамилия контакта.
        name (str): Имя контакта.
        patronymic (str): Отчество контакта.
        organization (str): Название организации контакта.
        work_phone (str): Рабочий телефонный номер контакта.
        personal_phone (str): Личный (сотовый) телефонный номер контакта.

    Методы:
        to_csv: Возвращает данные контакта в формате списка для сохранения в CSV-файл.
    """

    def __init__(
        self,
        surname: str,
        name: str,
        patronymic: str,
        organization: str,
        work_phone: str,
        personal_phone: str,
    ) -> None:
        """
        Инициализирует новый экземпляр класса Contact с заданными атрибутами.

        Параметры:
            surname (str): Фамилия контакта.
            name (str): Имя контакта.
            patronymic (str): Отчество контакта.
            organization (str): Название организации контакта.
            work_phone (str): Рабочий телефонный номер контакта.
            personal_phone (str): Личный (сотовый) телефонный номер контакта.
        """
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.organization = organization
        self.work_phone = work_phone
        self.personal_phone = personal_phone

    def to_csv(self) -> List[str]:
        """
        Форматирует данные контакта для сохранения в CSV.

        Возвращает:
            List[str]: Список строковых представлений атрибутов контакта.
        """
        return [
            self.surname,
            self.name,
            self.patronymic,
            self.organization,
            self.work_phone,
            self.personal_phone,
        ]
