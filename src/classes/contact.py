class Contact:
    """Класс для хранения информации о контакте."""

    def __init__(
        self,
        surname: str,
        name: str,
        patronymic: str,
        organization: str,
        work_phone: str,
        personal_phone: str,
    ) -> None:
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.organization = organization
        self.work_phone = work_phone
        self.personal_phone = personal_phone

    def to_csv(self) -> list:
        """Форматирует данные контакта для сохранения в CSV."""
        return [
            self.surname,
            self.name,
            self.patronymic,
            self.organization,
            self.work_phone,
            self.personal_phone,
        ]
