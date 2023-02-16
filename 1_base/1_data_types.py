########################################################################################################################
# TODO типы данных

from decimal import Decimal

# имя_переменной =(присваивание) значение_переменной

bool1 = True  # булевы значения в формате Правда/Ложь

int1 = 12  # целочисленные значения

float1 = 12.0  # значения с плавающей точкой

decimal1 = Decimal(12.0)  # значения с плавающей точкой, но для высокоточных расчётов

str1 = "Python"  # строка - коллекция символьных элементов
str2 = 'Python'  # строка - коллекция символьных элементов
str3 = "I'm"  # строка - коллекция символьных элементов
str4 = """I'm

man
"""  # строка - коллекция символьных элементов
str5 = "Python" + str(12.0)  # конкатенация (сложение строк)
str6 = f"Python {12.0}"  # интерполяция (вставка разных переменных в строку)
str7 = "Python \n \t float1"  # спец символы
str8 = r"Python \n \t float1"  # raw string
# "Python".encode() => b"Python"
# b"Python".decode() => "Python"

bytes1 = b"Python"  # байты - коллекция символьных элементов в виде байтов
bytes2 = b'\x01\x02\x03\x04\x05'
# b'\x016А\x02\x03\x04\x05' ASCII (256) vs UTF-8 (N миллионов)

list1 = [10, True, [], b"Python"]  # список - коллекция элементов

tuple1 = (12, False)  # кортеж - коллекция неизменяемых элементов

set1 = {12, False}  # множество - коллекция уникальных элементов

dict1 = {"Имя": "Python"}  # словарь - коллекция уникальных элементов в формате ключ-значение
dict2 = {
    "name": "Bogdan",
    "age": 25,
    "arr": [10, True, []],
    "dict1": {
        "name": "Bogdan",
        "age": 25,
        "arr": [10, True, []],
    },
}

dict3 = dict(Age=24, Name='Ally')  # создание словаря
print(dict3)

dict4 = {"Age": 24, "Name": 'Ally'}  # создание словаря
print(dict4)

dict5 = {"key_1": "va1", (10,): {"key1": "va1"}}  # ключом словаря может быть только неизменяемый тип данных
# (хэшируемый), т.е. он проходит через хэш функцию и генерирует уникальную комбинацию символов
# "контейнерные" типы данных могут быть ключом словаря, только при условии, что всё внутри хэшируемое

INT_CONSTANT = 12  # условно-неизменяемая
# print(INT_CONSTANT / 12)
# INT_CONSTANT = 13
is_commit = False  # можно изменить
IS_COMMIT = False  # можно изменить, но не желательно

########################################################################################################################

########################################################################################################################
# TODO действия с переменными

# вывод значение переменной в консоль
print(bool1)

# вывод значение типа переменной в консоль
type_bool1 = type(bool1)
print(type_bool1)
print(type(bool1))  # type_bool1 = type(bool1)

# проверка принадлежности типа данных
print(isinstance(bool1, str))  # False
print(isinstance(bool1, bool))  # True
print(isinstance(12, int))  # True

# конвертация типов данных:
float_to_int1 = int(10.5)  # int()
int_to_float1 = float(10)  # float()
str_to_float1 = float("10.2")  # float()
int_to_str1 = str(10.4)  # str()
int_to_bool1 = bool(0)  # bool()
set_to_list1 = list((1, 2, 2, 5))  # list()
# list_to_set1 = set([1, 2, 2, 5])  # set()
list_to_set1 = set(set_to_list1)  # set()
# ...

# получение ввода от пользователя
str_from_user1 = input("Введите Ваше имя: ")
print(str_from_user1)

# получение элементов из коллекции
#              0123456       -2-1
source_str1 = "Python is awesome"  # ['P', 'y', 't'...]

source_str2 = source_str1[2]
print(source_str2)  # t

source_str3 = source_str1[-2]
print(source_str3)  # m

source_str4 = source_str1[2:6:1]
print(source_str4)

#               0  1  2  3
source_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, [1, 2, 3, 4, 5, 6, 7, 8, 9]]

source_elem2 = source_list1[3]
print(source_elem2)

source_list2 = source_list1[2:5]
print(source_list2)

dict4 = {
    "name": "Bogdan",
    "age": 25,
    "arr": [10, True, []],
}
print(dict4["age"])
dict4["money"] = Decimal(12.0)
print(dict4)
del dict4["arr"]
print(dict4)

########################################################################################################################
