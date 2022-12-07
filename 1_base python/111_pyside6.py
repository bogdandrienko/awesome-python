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


