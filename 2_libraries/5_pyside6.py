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

########################################################################################################################

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

########################################################################################################################

import sys
import PySide6.QtWidgets as QtWidgets
import PySide6.QtGui as QtGui


class ExampleWindow(QtWidgets.QWidget):
    def __init__(self, window_name: str):
        super().__init__()

        self.window_name = window_name
        self.setGeometry(640, 480, 640, 480)
        self.setWindowTitle(self.window_name)
        self.layout = QtWidgets.QGridLayout()

        btn_quit = QtWidgets.QPushButton('нажми меня', self)
        btn_quit.clicked.connect(QtWidgets.QApplication.instance().quit)
        self.layout.addWidget(btn_quit, 0, 0)

        btn_1 = QtWidgets.QPushButton('', self)
        btn_1.clicked.connect(self.get_value_from_QLineEdit)
        self.layout.addWidget(btn_1, 0, 1)

        lbl1 = QtWidgets.QLabel(text="id", parent=self)
        self.layout.addWidget(lbl1, 1, 0)
        self.txt1 = QtWidgets.QLineEdit("-1", parent=self)
        self.layout.addWidget(self.txt1, 2, 0)

        lbl2 = QtWidgets.QLabel(text="name", parent=self)
        self.layout.addWidget(lbl2, 1, 1)
        txt2 = QtWidgets.QLineEdit("2", parent=self)
        self.layout.addWidget(txt2, 2, 1)

        lbl3 = QtWidgets.QLabel(text="surname", parent=self)
        self.layout.addWidget(lbl3, 1, 2)
        txt3 = QtWidgets.QLineEdit("2", parent=self)
        self.layout.addWidget(txt3, 2, 2)

        lbl4 = QtWidgets.QLabel("age", parent=self)
        self.layout.addWidget(lbl4, 1, 3)
        txt4 = QtWidgets.QLineEdit("4", parent=self)
        self.layout.addWidget(txt4, 2, 3)

        lbl5 = QtWidgets.QLabel("salary", parent=self)
        self.layout.addWidget(lbl5, 1, 4)
        txt5 = QtWidgets.QLineEdit("5", self)
        self.layout.addWidget(txt5, 2, 4)

        self.setLayout(self.layout)

        self.show()

    def get_value_from_QLineEdit(self):
        print(f"{self.txt1.text()}  !!!")

    def print_hello_world(self):
        print(f"{self.window_name} hello!")

    def closeEvent(self, event: QtGui.QCloseEvent):
        reply = QtWidgets.QMessageBox.question(self, 'Внимание', 'Вы действительно хотите выйти?',
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = ExampleWindow('Наше приложение на PySide6')
    sys.exit(app.exec())

# id = -1
# name = 3
# surname = 3
# age = 4
# salary = 5

########################################################################################################################


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


########################################################################################################################


import datetime
import sys
import time

import requests
from bs4 import BeautifulSoup
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QComboBox
import threading

values = [{"name": "", "value": 0}]


def get_fresh_values():
    while True:

        current_time = datetime.datetime.now().strftime("%S")

        if int(current_time) // 10 % 2:
            print('задержка')
            time.sleep(10)

        print(f"Seconds: {current_time}")

        # time.sleep(1)

        url = 'https://myfin.by/converter.html'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/102.0.0.0 Safari/537.36'
        }
        response = requests.get(url=url, headers=headers)

        with open('new_html.html', 'wb') as file:
            file.write(response.content)

        soup = BeautifulSoup(response.text, 'lxml')

        print(soup)
        # print(soup.text)

        # data = soup.find_all('div', class_="converter-container__item")

        data = soup.findAll("input", class_="input_calc form-control form-input-sum bestmb")

        print(data)

        values = []
        for i in data:
            print(i, '\n')

            sep_name_left = 'id="bestmb_'
            sep_name_right = '" inputmode'

            val_name_1 = str(i).split(sep=sep_name_left)[1]
            val_name_2 = val_name_1.split(sep=sep_name_right)[0]

            print(val_name_2, '\n')

            sep_value_left = 'value="'
            sep_value_right = '"/>'

            val_value_1 = str(i).split(sep=sep_value_left)[1]
            val_value_2 = val_value_1.split(sep=sep_value_right)[0]

            print(val_value_2, '\n')

            dict_value = {
                "name": val_name_2,
                "value": val_value_2,
            }
            values.append(dict_value)

        print(values)


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.line_edit = QLineEdit()
        layout.addWidget(self.line_edit)

        self.label = QLabel()
        layout.addWidget(self.label)

        self.line_edit.textChanged.connect(self.line_edit_text_changed)

        self.combo_box_filter = QComboBox()
        self.combo_box_filter.addItem("usd")
        self.combo_box_filter.addItem("eur")
        self.combo_box_filter.addItems(["gbp", "cny", "pln", "rub"])

        layout.addWidget(self.combo_box_filter)  # вкладываем QComboBox -> QGridLayout

        self.show()

    def line_edit_text_changed(self, text):
        try:
            combo = self.combo_box_filter.currentText()
            print(combo)

            for dictionary in values:  # массив со словарями
                keys1 = dictionary.keys()

                print(keys1)

                values1 = dictionary.values()

                print(values1)

                item1 = dictionary.items()

                print(item1)

                # if combo in values1:
                #     print('валюта есть')
                #     text = round(float(dictionary["value"]) * float(text), 3)
                #     self.label.setText("Ваша сумма: " + str(text) + " единиц")
                # else:
                #     print('валюты нет')

                if dictionary["name"] == combo:
                    print('валюта есть')
                    text = round(float(dictionary["value"]) * float(text), 3)
                    self.label.setText("Ваша сумма: " + str(text) + " единиц")

        except Exception as error:
            self.label.setText('ошибка ввода данных')


threading.Thread(target=get_fresh_values).start()

app = QApplication(sys.argv)
mw = MainWindow()
app.exec()

########################################################################################################################

########################################################################################################################

# прочитать изображение в память (подать путь к изображению - от пользователя) - чтение с диска
# выдать данных об изображении
# обработка изображения (подать все нужные параметры - от пользователя)
# выдать данных об итоговом изображении
# запись (сохранение результата) - перезапись/или сохранить как

import sys
import time
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QGridLayout, QCheckBox, QPushButton, QSlider, \
    QComboBox
import cv2  # pip install opencv-python


class MainWindow(QWidget):  # MainWindow - класс наследник(дочерний) от класса QWidget(родитель)
    def __init__(self, width=640, height=480, title="title"):
        QWidget.__init__(self)  # тут происходит вызов конструктора для родителя

        self.setWindowTitle(title)
        self.resize(width, height)

        self.image_data = None

        # layout = QVBoxLayout()
        # self.setLayout(layout)
        #
        # self.line_edit = QLineEdit()
        # layout.addWidget(self.line_edit)
        #
        # self.line_edit1 = QLineEdit()
        # layout.addWidget(self.line_edit1)
        #
        # self.label = QLabel()
        # layout.addWidget(self.label)

        self.layout = QGridLayout()  # экземпляр класса интерфейса grid(сетка)
        self.setLayout(self.layout)  # вкладываем QGridLayout -> MainWindow(QWidget)

        self.label_path = QLabel('Путь к файлу: ')  # экзампляр строки текста
        self.layout.addWidget(self.label_path, 1, 1)

        self.line_edit_path = QLineEdit('image_data/dino.jpg')  # экзампляр строки ввода текста
        self.layout.addWidget(self.line_edit_path, 2, 1)  # вкладываем QLineEdit -> QGridLayout

        self.label_check = QLabel('Статус: ')  # экзампляр строки текста
        self.layout.addWidget(self.label_check, 1, 2)

        self.check_box_status = QCheckBox()  # экзампляр чек бокса
        self.check_box_status.setChecked(False)
        self.layout.addWidget(self.check_box_status, 2, 2)  # вкладываем QCheckBox -> QGridLayout

        self.push_button_check = QPushButton('проверить наличие файла')  # экзампляр строки ввода текста
        self.push_button_check.clicked.connect(self.read_and_check_image_in_path)
        # self.push_button_check.setGeometry(QtCore.QRect(200, 150, 93, 28))
        self.layout.addWidget(self.push_button_check, 2, 3)  # вкладываем QLineEdit -> QGridLayout

        self.label_width = QLabel('Ширина: ')
        self.layout.addWidget(self.label_width, 3, 1)

        self.label_height = QLabel('Высота: ')
        self.layout.addWidget(self.label_height, 3, 2)

        self.line_edit_width = QLineEdit('0')  # экзампляр строки ввода текста
        self.layout.addWidget(self.line_edit_width, 4, 1)  # вкладываем QLineEdit -> QGridLayout

        self.line_edit_height = QLineEdit('0')  # экзампляр строки ввода текста
        self.layout.addWidget(self.line_edit_height, 4, 2)  # вкладываем QLineEdit -> QGridLayout

        self.check_box_wb = QCheckBox()  # экзампляр чек бокса
        self.check_box_wb.setChecked(False)
        self.layout.addWidget(self.check_box_wb, 5, 1)  # вкладываем QCheckBox -> QGridLayout

        self.label_check_wb = QLabel('сделать чёрно-белым: ')  # экзампляр строки текста
        self.layout.addWidget(self.label_check_wb, 5, 2)

        self.check_box_protect = QCheckBox()  # экзампляр чек бокса
        self.check_box_protect.setChecked(False)
        self.check_box_protect.stateChanged.connect(self.protect)
        self.layout.addWidget(self.check_box_protect, 5, 3)  # вкладываем QCheckBox -> QGridLayout

        self.label_check_box_protect = QLabel('подтвердить изменения: ')  # экзампляр строки текста
        self.layout.addWidget(self.label_check_box_protect, 5, 4)

        # self.slider_quality = QSlider(Qt.Horizontal)
        self.slider_quality = QSlider()
        self.slider_quality.setMinimum(1)
        self.slider_quality.setMaximum(100)
        self.slider_quality.setValue(95)
        self.layout.addWidget(self.slider_quality, 4, 5)

        self.label_slider_quality = QLabel('качество: ')  # экзампляр строки текста
        self.layout.addWidget(self.label_slider_quality, 5, 5)

        self.label_1 = QLabel('')
        self.layout.addWidget(self.label_1, 6, 1)

        self.push_button_start = QPushButton('выполнить')  # экзампляр строки ввода текста
        self.push_button_start.clicked.connect(self.start)
        self.push_button_start.setEnabled(False)
        # self.push_button_check.setGeometry(QtCore.QRect(200, 150, 93, 28))
        self.layout.addWidget(self.push_button_start, 7, 1)  # вкладываем QLineEdit -> QGridLayout

        self.push_button_stop = QPushButton('отменить')  # экзампляр строки ввода текста
        self.push_button_stop.clicked.connect(self.stop)
        # self.push_button_check.setGeometry(QtCore.QRect(200, 150, 93, 28))
        self.layout.addWidget(self.push_button_stop, 7, 3)  # вкладываем QLineEdit -> QGridLayout

        self.combo_box_filter = QComboBox()
        self.combo_box_filter.addItem("гаусс")
        self.combo_box_filter.addItem("фильтр 2")
        self.combo_box_filter.addItems(["фильтр 3", "фильтр 4", "фильтр 5"])

        self.layout.addWidget(self.combo_box_filter, 7, 4)  # вкладываем QComboBox -> QGridLayout

        # self.line_edit1 = QLineEdit()  # экзампляр строки ввода текста
        # self.layout2.addWidget(self.line_edit1)  # вкладываем QLineEdit -> QGridLayout
        #
        # self.line_edit2 = QLineEdit()  # экзампляр строки ввода текста
        # self.layout2.addWidget(self.line_edit2, 2, 2)  # вкладываем QLineEdit -> QGridLayout

        # self.line_edit3 = self.render_line_edit(self.layout2, '111111111', 2, 2)

        # self.line_edit3 = QLineEdit()  # экзампляр строки ввода текста
        # self.layout2.addWidget(self.line_edit3)  # вкладываем QLineEdit -> QGridLayout

        # self.line_edit.textChanged.connect(self.line_edit_text_changed)

        def delay(seconds: float):
            time.sleep(seconds)
            # тут код(поток исполнения)
            self.show()
        delay(0.5)
        # self.show()

    def read_and_check_image_in_path(self):

        value = self.line_edit_path.text()
        print(value)

        # тут мы будем проверять наличие файла по пути в строке

        # opencv
        # self.image_data = пиксели

        # C:\Project\Github_Projects\PyE-221-1\dino.jpg - абсолютный
        # dino.jpg - относительный
        # img1 = cv2.imread(value, cv2.IMREAD_GRAYSCALE)  # читаем изображение по пути, с флагом для серого
        # cv2.imshow('dino_window1', img1)  # рендерит(отрисовывает на экране) массив пикселей - изображение

        try:
            img2 = cv2.imread(value, cv2.IMREAD_COLOR)  # читаем изображение по пути, с флагом для цветного
        except Exception as error:
            print(error)
            img2 = []

        print(img2)
        print(len(img2))
        print(type(img2))

        if len(img2) > 0:  # [] - False, [''] - True, '' - False, '1' - True
            cv2.imshow('dino_window2', img2)  # рендерит(отрисовывает на экране) массив пикселей - изображение
            cv2.waitKey(1)  # для задержки отображения кадра (если изображение, то нужен параметр 1)
            # cv2.imwrite('dino2.jpg', img)

            has_file = True
            print('изображение успешно прочитано')

            self.image_data = img2
            print(self.image_data.shape)
            # height, width = self.image_data.shape[:2]  # -> (1920, 1080)
            height, width, channels = self.image_data.shape  # -> (1920, 1080, 3)

            self.line_edit_width.setText(str(width))
            self.line_edit_height.setText(str(height))

        else:
            has_file = False
            print('изображение не прочитано!')

            self.line_edit_width.setText("0")
            self.line_edit_height.setText("0")

        self.check_box_status.setChecked(has_file)

        # self.push_button_check.hide()  # прятать элемент интерфейса

    def start(self):
        print("start")

        # combo = self.combo_box_filter.itemText(3)
        combo = self.combo_box_filter.currentText()
        print(combo)

        white_black = bool(self.check_box_wb.isChecked())

        quality = int(self.slider_quality.value())
        width = int(self.line_edit_width.text())
        height = int(self.line_edit_height.text())

        image = self.image_data
        print(type(image))

        if white_black:
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # BGR(RGB) -> GRAY
            image = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)[1]  # GRAY -> WHITE

        # value = 100  # 0 -> 255
        # if value > 127:
        #     value = 1
        # else:
        #     value = 0

        image = cv2.resize(image, (width, height))

        # 0 200 400
        #  150 250
        # image = image[150:250:1]  # обрезка

        cv2.imwrite("image_data/dino_new.jpg", image, [cv2.IMWRITE_JPEG_QUALITY, quality])

    def stop(self):
        print("stop")
        pass

    def protect(self):
        self.push_button_start.setEnabled(self.check_box_protect.isChecked())

    def render_line_edit(self, parent, default="", row=1, col=1):
        new = QLineEdit(default)
        parent.addWidget(new, row, col)
        return new

    def create_line_edit(self):
        self.layout.addWidget(QLineEdit())
        return

    # def line_edit_text_changed(self, text):
    #     try:
    #         text = round(course_dollar * float(text), 3)
    #         self.label.setText("Ваша сумма: " + str(text) + " $")
    #     except Exception as error:
    #         self.label.setText('ошибка ввода данных')


app = QApplication(sys.argv)
mw = MainWindow(640, 480, 'image analyse')  # создаём инстанс (экземпляр) класса
# пока класс не умрёт, эта часть кода не затронется
app.exec()  # очистка памяти

app1 = QApplication(sys.argv)
app1.exec()


########################################################################################################################
