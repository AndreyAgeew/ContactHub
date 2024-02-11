from validators import validate_name, validate_organization, validate_phone_number, validtate_patronymic


def _input_with_validation(prompt: str, validation_function, error_message: str) -> str:
    """Запрашивает ввод у пользователя до тех пор, пока ввод не пройдет проверку валидацией."""
    while True:
        value = input(prompt)
        if validation_function(value):
            return value
        else:
            print(error_message)


def get_surname() -> str:
    """Возвращает фамилию"""
    return _input_with_validation(
        "Фамилия: ", validate_name, "Фамилия должна содержать только буквы."
    )


def get_name() -> str:
    """Возвращает имя"""
    return _input_with_validation(
        "Имя: ", validate_name, "Имя должно содержать только буквы."
    )


def get_patronymic() -> str:
    """Возвращает отчество"""
    return _input_with_validation(
        "Отчество (если есть): ",
        validtate_patronymic,
        "Отчество должно содержать только буквы.",
    )


def get_organization() -> str:
    """Возвращает название организации"""
    return _input_with_validation(
        "Организация: ",
        validate_organization,
        "Название организации не может быть пустым.",
    )


def get_work_phone() -> str:
    """Возвращает рабочий телефон"""
    return _input_with_validation(
        "Рабочий телефон: ", validate_phone_number, "Неверный формат рабочего телефона."
    )


def get_personal_phone() -> str:
    """Возвращает личный телефон"""
    return _input_with_validation(
        "Личный телефон: ", validate_phone_number, "Неверный формат личного телефона."
    )
