import re


def _validate_non_empty(value: str) -> bool:
    """Служебный валидатор, проверяет, что строка не пустая."""
    return bool(value.strip())


def validate_phone_number(phone_number: str) -> bool:
    """Проверяет, соответствует ли номер телефона базовым требованиям формата."""
    pattern = r"^\+?\d{10,15}$"  # Простая регулярка: международный формат, 10-15 цифр.
    return re.match(pattern, phone_number) is not None


def validate_name(name: str) -> bool:
    """Проверяет, что имя содержит только буквы, и не пустое."""
    pattern = r"^[A-Za-zА-Яа-яЁё]+$"
    return bool(re.match(pattern, name.strip()))


def validtate_patronymic(patronymic: str) -> bool:
    """Проверяет, что отчество содержит только буквы или пустое."""
    if patronymic == "":
        return True  # Допускаем пустую строку
    pattern = r"^[A-Za-zА-Яа-яЁё]+$"
    return bool(re.match(pattern, patronymic.strip()))


def validate_surname(surname: str) -> bool:
    """Проверяет, что фамилия содержит только буквы, и не пустое."""
    return validate_name(surname)


def validate_organization(organization: str) -> bool:
    """Проверяет, что название организации не пустое (можно добавить дополнительные условия)."""
    return _validate_non_empty(organization)
