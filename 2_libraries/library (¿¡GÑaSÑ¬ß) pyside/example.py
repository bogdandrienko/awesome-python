import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget, QGridLayout,
)
import aiohttp
import asyncio
import json


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Analyse")

        # self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
        # self.button = QtWidgets.QPushButton("File")
        # self.text = QtWidgets.QLabel("Hello World")
        # self.layout = QtWidgets.QVBoxLayout(self)
        # self.layout.addWidget(self.text)
        # self.layout.addWidget(self.button)
        #
        # self.button.clicked.connect(self.magic)

        # self.layout1 = QVBoxLayout()
        # self.layout1 = QtWidgets.QVBoxLayout(self)
        # widgets = [
        #     QCheckBox,
        #     QComboBox,
        #     QDateEdit,
        #     QDateTimeEdit,
        #     QDial,
        #     QDoubleSpinBox,
        #     QFontComboBox,
        #     QLCDNumber,
        #     QLabel,
        #     QLineEdit,
        #     QProgressBar,
        #     QPushButton,
        #     QRadioButton,
        #     QSlider,
        #     QSpinBox,
        #     QTimeEdit,
        # ]
        #
        # for w in widgets:
        #     self.layout1.addWidget(w())
        # self.layout3 = QtWidgets.QVBoxLayout(self)

        # self.layout1 = QVBoxLayout()
        # self.layout1 = QtWidgets.QVBoxLayout(self)
        # widgets = [
        #     QCheckBox,
        #     QComboBox,
        #     QDateEdit,
        #     QDateTimeEdit,
        #     QDial,
        #     QDoubleSpinBox,
        #     QFontComboBox,
        #     QLCDNumber,
        #     QLabel,
        #     QLineEdit,
        #     QProgressBar,
        #     QPushButton,
        #     QRadioButton,
        #     QSlider,
        #     QSpinBox,
        #     QTimeEdit,
        # ]
        #
        # for w in widgets:
        #     self.layout1.addWidget(w())

        # мы создаём сетку для отображения всех виджетов
        self.layout5 = QGridLayout()
        self.layout5 = QtWidgets.QGridLayout(self)

        # создаём кнопку
        self.button = QPushButton("request")
        self.layout5.addWidget(self.button, 2, 2)
        # присоединяем к кнопке
        self.button.clicked.connect(self.request)

        # наименование api-пути
        self.layout5.addWidget(QLabel("path"), 0, 1)

        # значение api-пути
        self.path_edit = QLineEdit("http://192.168.1.121/api/result/")
        self.layout5.addWidget(self.path_edit, 1, 1)

        self.layout5.addWidget(QLabel("params"), 0, 2)

        self.params_edit = QLineEdit("")
        self.layout5.addWidget(self.params_edit, 1, 2)

        self.result_label = QLabel("result")
        self.layout5.addWidget(self.result_label, 3, 1)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        # self.setCentralWidget(widget)

    @QtCore.Slot()
    def request(self):
        path = self.path_edit.text()
        params = {"value": self.params_edit.text()}

        async def main():
            async with aiohttp.ClientSession() as session:

                if len(params["value"]) > 0:
                    async with session.post(path, data=params) as response:
                        html = await response.text()
                else:
                    async with session.get(path) as response:
                        # print("Status:", response.status)
                        # print("Content-type:", response.headers['content-type'])

                        # html = await response.text()
                        html = await response.text()
                        print(type(html))
                        html = json.loads(html)
                        print(type(html))
                        print("Body:", html)


                        # if type(html["recepts"]) == type(""):
                        #     self.result_label.setText(html["recepts"])
                        # elif type(html["recepts"]) == type([]):
                        #     for i in html["recepts"]:
                        #         str1 += f'{i}\n'
                        #     self.result_label.setText(str1)
                        # else:
                        #     self.result_label.setText("ошибка")
                        if isinstance(html["recepts"], str):
                            # печатает текст отсутствия рецепта
                            self.result_label.setText(html["recepts"])
                        elif isinstance(html["recepts"], list):
                            str1 = ''
                            for i in html["recepts"]:
                                str1 += f'{i}\n'
                            self.result_label.setText(str1)
                        else:
                            self.result_label.setText("ошибка")

        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.resize(1280, 720)
    widget.show()
    sys.exit(app.exec())
    
    
##############################################################################################


class PySideClass:
    @staticmethod
    def example():
        def play_func(data):
            global play
            play = False
            sleep(0.5)
            play = True

            def whiles():
                print(data)

            thread_render = Thread(target=whiles)
            thread_render.start()
            widget.set_text_func('завершено')

        class MyWidget(QtWidgets.QWidget):
            def __init__(self, title="ожидание"):
                super().__init__()
                self.play_button = QtWidgets.QPushButton("play")
                self.temp_box = QtWidgets.QDoubleSpinBox()
                self.stop_button = QtWidgets.QPushButton("stop")
                self.quit_button = QtWidgets.QPushButton("quit")
                self.temp_box.setValue(36.6)
                self.setWindowTitle(title)

                self.ui_window = QtWidgets.QHBoxLayout(self)
                self.ui_window.addWidget(self.play_button)
                self.ui_window.addWidget(self.temp_box)
                self.ui_window.addWidget(self.stop_button)
                self.ui_window.addWidget(self.quit_button)

                self.play_button.clicked.connect(self.play_btn_func)
                self.stop_button.clicked.connect(self.stop_btn_func)
                self.quit_button.clicked.connect(self.quit_btn_func)

            def play_btn_func(self):
                self.set_text_func("в процессе")
                play_func(data=self.temp_box.value())

            def stop_btn_func(self):
                self.set_text_func("пауза")
                global play
                play = False

            def quit_btn_func(self):
                self.set_text_func("выйти")
                global play
                play = False
                global app
                sys.exit(app.exec())

            def set_text_func(self, text: str):
                self.setWindowTitle(text)

        if __name__ == "__main__":
            play = False
            app = QtWidgets.QApplication([])
            widget = MyWidget()
            widget.resize(640, 480)
            thread_main = Thread(target=widget.show())
            thread_main.start()
            sys.exit(app.exec())
            
            
##################################################################################################

import sys
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import (
    QCheckBox,
    QLabel,
    QLineEdit,
    QPushButton,
)
import json
import requests
import aiohttp
import asyncio
import threading
import multiprocessing


class MyUserInterfaceClass(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QGridLayout(self)

        self.label_path = QLabel("path")
        self.layout.addWidget(self.label_path, 0, 0)
        self.line_edit_path = QLineEdit("http://127.0.0.1:8000/api/create_user/")
        self.layout.addWidget(self.line_edit_path, 0, 1)

        self.label_username = QLabel("username")
        self.layout.addWidget(self.label_username, 1, 0)
        self.line_edit_username = QLineEdit("username")
        self.layout.addWidget(self.line_edit_username, 1, 1)

        self.label_password1 = QLabel("password1")
        self.layout.addWidget(self.label_password1, 2, 0)
        self.line_edit_password1 = QLineEdit("password1")
        self.layout.addWidget(self.line_edit_password1, 2, 1)

        self.label_password2 = QLabel("password2")
        self.layout.addWidget(self.label_password2, 3, 0)
        self.line_edit_password2 = QLineEdit("password2")
        self.layout.addWidget(self.line_edit_password2, 3, 1)

        self.check_box_is_equal = QCheckBox("")
        self.layout.addWidget(self.check_box_is_equal, 2, 2)
        self.label_is_equal = QLabel("")
        self.layout.addWidget(self.label_is_equal, 3, 2)

        self.result_label = QLabel("result")
        self.layout.addWidget(self.result_label, 4, 0)
        self.button = QPushButton("request")
        self.layout.addWidget(self.button, 4, 1)
        # self.button.clicked.connect(self.sync_request)
        self.button.clicked.connect(self.async_request)

        self.setWindowTitle("Create user in Django")
        self.resize(640, 480)
        self.show()

    @QtCore.Slot()
    def sync_request(self):
        url = self.line_edit_path.text()
        username = self.line_edit_username.text()
        password1 = self.line_edit_password1.text()
        password2 = self.line_edit_password2.text()
        if password1 != password2:
            self.check_box_is_equal.setChecked(False)
            self.label_is_equal.setText("пароли не совпадают!")
        else:
            self.check_box_is_equal.setChecked(True)
            self.label_is_equal.setText("")
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                     "Chrome/51.0.2704.103 Safari/537.36"}
            response = requests.post(
                url=url,
                data={"username": username, "password": password1},
                headers=headers
            )
            json_data = json.loads(response.content)
            self.result_label.setText(json_data["result"])

    @QtCore.Slot()
    def async_request(self):
        url = self.line_edit_path.text()
        username = self.line_edit_username.text()
        password1 = self.line_edit_password1.text()
        password2 = self.line_edit_password2.text()
        if password1 != password2:
            self.check_box_is_equal.setChecked(False)
            self.label_is_equal.setText("пароли не совпадают!")
        else:
            self.check_box_is_equal.setChecked(True)
            self.label_is_equal.setText("")
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                     "Chrome/51.0.2704.103 Safari/537.36"}

            async def async_function():
                async with aiohttp.ClientSession() as session:
                    async with session.post(
                            url=url, data={"username": username, "password": password1}, headers=headers
                    ) as response:
                        json_data = await response.json()
                        self.result_label.setText(json_data["result"])

            asyncio.get_event_loop().run_until_complete(async_function())


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    ui = MyUserInterfaceClass()
    sys.exit(app.exec())