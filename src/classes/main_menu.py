from .management_mixin import ContactManagementMixin
from .phonebook import PhoneBook


class MainMenuMeta(type):
    """
    Метакласс для управления процессом создания и запуска экземпляра MainMenu.
    """

    def __call__(cls, *args, **kwargs):
        """
        Создает экземпляр класса и инициирует интерактивное меню пользователя.
        """
        instance = super().__call__(*args, **kwargs)
        instance._run()
        return instance


class MainMenu(ContactManagementMixin, metaclass=MainMenuMeta):
    """
    Главное меню приложения для взаимодействия с пользователем.
    Позволяет просматривать, добавлять, искать м обновлять контакты.
    """

    phonebook = PhoneBook("contacts.csv")

    def _run(self):
        """
        Отображает главное меню и обрабатывает выбор пользователя.
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
                print("Некорректный выбор. Пожалуйста, введите число от 1 до 4.")
