from typing import Any

from .management_mixin import ContactManagementMixin
from .phonebook import PhoneBook


class MainMenuMeta(type):
    """
    Метакласс для управления процессом создания и запуска экземпляра MainMenu.

    Этот метакласс переопределяет метод __call__, чтобы автоматически запускать
    интерактивное меню пользователя при создании экземпляра класса MainMenu.
    """

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        """
        Создает экземпляр класса и инициирует интерактивное меню пользователя.

        Args:
            *args: Переменное количество аргументов, передаваемых конструктору класса.
            **kwargs: Переменное количество именованных аргументов, передаваемых конструктору класса.

        Returns:
            Экземпляр класса, для которого был вызван метакласс.
        """
        instance = super().__call__(*args, **kwargs)
        instance._run()
        return instance


class MainMenu(ContactManagementMixin, metaclass=MainMenuMeta):
    """
    Главное меню приложения для взаимодействия с пользователем.
    Позволяет просматривать, добавлять, искать и обновлять контакты.

    Attributes:
        phonebook (PhoneBook): Экземпляр класса PhoneBook для управления контактами.
    """

    phonebook = PhoneBook("contacts.csv")

    def _run(self) -> None:
        """
        Отображает главное меню и обрабатывает выбор пользователя.

        В бесконечном цикле выводит меню с опциями и обрабатывает ввод пользователя,
        выполняя соответствующие действия в зависимости от выбранного пункта меню.
        """
        while True:
            print("\n1. Показать все контакты")
            print("2. Добавить контакт")
            print("3. Найти контакт по фамилии")
            print("4. Изменить данные контакта по личному номеру телефона")
            print("5. Выход\n")

            choice = input("Выберите действие: ")

            if choice == "1":
                self.phonebook.display_contacts()
            elif choice == "2":
                self._add_contact()
            elif choice == "3":
                self._find_contact()
            elif choice == "4":
                self._edit_contact()
            elif choice == "5":
                break
            else:
                print("Некорректный выбор. Пожалуйста, введите число от 1 до 5.")
