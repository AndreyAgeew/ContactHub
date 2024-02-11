from typing import Callable, List

from classes.contact import Contact
from validators import (
    validate_name,
    validate_organization,
    validate_personal_phone_number,
    validate_work_phone_number,
    validtate_patronymic,
)


def _input_with_validation(
    prompt: str, validation_function: Callable[..., bool], error_message: str, **kwargs
) -> str:
    """
    Запрашивает ввод у пользователя до тех пор, пока ввод не пройдет проверку валидацией.

    Args:
        prompt (str): Сообщение для отображения пользователю.
        validation_function (Callable[..., bool]): Функция валидации, принимающая введенное значение и возвращающая bool.
        error_message (str): Сообщение об ошибке, отображаемое при неудачной валидации.
        **kwargs: Дополнительные аргументы, передаваемые в функцию валидации.

    Returns:
        str: Строка, прошедшая проверку валидацией.
    """
    while True:
        value = input(prompt)
        if validation_function(value, **kwargs):
            return value
        else:
            print(error_message)


def get_surname() -> str:
    """Возвращает фамилию, прошедшую валидацию."""
    return _input_with_validation(
        "Фамилия: ", validate_name, "Фамилия должна содержать только буквы."
    )


def get_name() -> str:
    """Возвращает имя, прошедшее валидацию."""
    return _input_with_validation(
        "Имя: ", validate_name, "Имя должно содержать только буквы."
    )


def get_patronymic() -> str:
    """Возвращает отчество, прошедшее валидацию."""
    return _input_with_validation(
        "Отчество (если есть): ",
        validtate_patronymic,
        "Отчество должно содержать только буквы или быть пустым.",
    )


def get_organization() -> str:
    """Возвращает название организации, прошедшее валидацию."""
    return _input_with_validation(
        "Организация: ",
        validate_organization,
        "Название организации не может быть пустым.",
    )


def get_work_phone() -> str:
    """Возвращает рабочий телефон, прошедший валидацию."""
    return _input_with_validation(
        "Рабочий телефон: ",
        validate_work_phone_number,
        "Неверный формат рабочего телефона.",
    )


def get_personal_phone(records: List[Contact]) -> str:
    """
    Возвращает личный телефон, прошедший валидацию и проверку на уникальность.

    Args:
        records (List[Contact]): Список текущих контактов для проверки уникальности номера.

    Returns:
        str: Личный телефон, прошедший валидацию и уникальный среди записей.
    """
    return _input_with_validation(
        "Личный телефон: ",
        validate_personal_phone_number,
        "Неверный формат личного телефона или номер уже есть в справочнике",
        records=records,
    )
