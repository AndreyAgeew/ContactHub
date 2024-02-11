import re
from typing import List

from classes.contact import Contact


def _validate_non_empty(value: str) -> bool:
    """
    Проверяет, что строка не пустая.

    Args:
        value (str): Строка для проверки.

    Returns:
        bool: True, если строка не пустая, иначе False.
    """
    return bool(value.strip())


def _is_unique_phone_number(phone_number: str, records: List[Contact]) -> bool:
    """
    Проверяет уникальность номера телефона среди списка контактов.

    Args:
        phone_number (str): Номер телефона для проверки.
        records (List[Contact]): Список контактов для сравнения.

    Returns:
        bool: True, если номер уникален, иначе False.
    """
    return all(phone_number != contact.personal_phone for contact in records)


def validate_work_phone_number(phone_number: str) -> bool:
    """
    Проверяет, соответствует ли рабочий номер телефона базовым требованиям формата.

    Args:
        phone_number (str): Рабочий номер телефона для проверки.

    Returns:
        bool: True, если номер соответствует формату, иначе False.
    """
    pattern = r"^\+?\d{10,15}$"
    return re.match(pattern, phone_number) is not None


def validate_personal_phone_number(phone_number: str, records: List[Contact]) -> bool:
    """
    Проверяет, соответствует ли личный номер телефона базовым требованиям формата и уникален ли он.

    Args:
        phone_number (str): Личный номер телефона для проверки.
        records (List[Contact]): Список контактов для проверки уникальности.

    Returns:
        bool: True, если номер соответствует формату и уникален, иначе False.
    """
    pattern = r"^\+?\d{10,15}$"
    return re.match(pattern, phone_number) is not None and _is_unique_phone_number(
        phone_number, records
    )


def validate_name(name: str) -> bool:
    """
    Проверяет, что имя содержит только буквы и не пустое.

    Args:
        name (str): Имя для проверки.

    Returns:
        bool: True, если имя соответствует требованиям, иначе False.
    """
    pattern = r"^[A-Za-zА-Яа-яЁё]+$"
    return bool(re.match(pattern, name.strip()))


def validtate_patronymic(patronymic: str) -> bool:
    """
    Проверяет, что отчество содержит только буквы или пустое.

    Args:
        patronymic (str): Отчество для проверки.

    Returns:
        bool: True, если отчество соответствует требованиям или пустое, иначе False.
    """
    if patronymic == "":
        return True
    pattern = r"^[A-Za-zА-Яа-яЁё]+$"
    return bool(re.match(pattern, patronymic.strip()))


def validate_surname(surname: str) -> bool:
    """
    Проверяет, что фамилия содержит только буквы и не пустая.

    Args:
        surname (str): Фамилия для проверки.

    Returns:
        bool: True, если фамилия соответствует требованиям, иначе False.
    """
    return validate_name(surname)


def validate_organization(organization: str) -> bool:
    """
    Проверяет, что название организации не пустое.

    Args:
        organization (str): Название организации для проверки.

    Returns:
        bool: True, если название организации не пустое, иначе False.
    """
    return _validate_non_empty(organization)
