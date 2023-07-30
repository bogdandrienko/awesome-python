"""Главный файл"""


class MeClass:
    """Вспомогательный класс"""

    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, value):
        try:
            self.value = int(value)
        except ValueError:
            print("Неверный формат!")


class UserIsActive:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        redis = {
            "todos": [{}],
            "rooms": [{}],
            "active":{1: True, }
        }

        import sqlite3

        """
        id = 1
        user_id = User(id)
        time_connect = 1
        """
        # REST
        pass

    def get_status(self, user_id: int) -> bool:
        if user_id < 0:
            return False
            # raise ValueError("Пользователь не найден")

        if (time_connect - datetime.datetime.now()) > 5 * 60 * 60:
            return False

        # todo только если в базе есть с статусом 1
        return True
    def set_active(self, user_id: int):
        # INSERT
        pass
