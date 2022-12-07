# виртуальное окружение - новая версия интерпретатора с зависимостями (модули и библиотеки)
#! для каждого проекта своё виртуальное окружение и свои библиотеки !

# обновление глобального пакетного менеджера
python.exe -m pip install --upgrade pip

# установка библиотеки для создания виртуального окружения глобально
pip install env

# создание нового виртуального окружения
python -m venv "имя нового виртуального окружения" (venv/env)
python -m venv env

# активация виртуального окружения
call env/Scripts/activate.bat
deactivate

# обновление локального пакетного менеджера
python.exe -m pip install --upgrade pip

# установка библиотек внутрь виртуального окружения
pip install openpyxl
pip install requests

# "заморозка" всех библиотек внутри виртуального окружения
pip freeze > requirements.txt

# установка всех библиотек строго по версиям из файла
pip install -r requirements.txt

#########################
# linux

python3 -m venv env
source env/bin/activate
pip install openpyxl
pip install requests
pip freeze > requirements.txt

#########################
