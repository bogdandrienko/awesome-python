########################################################################################################################
# TODO list comprehension

import random
from typing import Union

# новый массив с квадратами значений другого
list1 = [1, 2, 3, 4, 5]
list2 = []
for i in list1:
    result = i ** 2
    list2.append(result)
print(list2)

# простейший пример
list3 = [i ** 2 for i in [1, 2, 3, 4, 5]]
print(list3)

# пример с условием
list4 = [i ** 2 for i in [1, 2, 3, 4, 5] if i % 2 != 0]
print(list4)

# пример для генерации массива словарей
list5 = [1, 2, 3, 4, 5]
list6 = []
for i in list5:
    if i % 2 != 0:
        result = {f"key_{i}": i}
        list6.append(result)
print(list6)

# пример для генерации массива словарей
list7 = [{f"key_{i}": i} for i in [1, 2, 3, 4] if i % 2 != 0]
print(list7)

list8 = [" apple ", " banana ", " cherry ", "kiwi ", " mango"]
list9 = [str(char).strip() for char in list8 if "i" in char and len(str(char).strip()) > 3]
print(list9)

list10 = [str(x).strip() for x in "Яблоко, банан, груша       , киви      ".split(",")]
print(list10)

# TODO ещё пример


def return_random_word(arr_words: Union[list[str]]) -> str:
    return random.choice(arr_words)


def random_passwrd(length: int, chars="1234567890srjuvbrviuabrviluaerb!@-"):
    if length <= 0 or len(chars) <= 0:
        raise ArithmeticError
    password = ""
    while len(password) < length:
        password += random.choice(chars)
    return password


print(return_random_word(arr_words=["Аня", "Надя", "Катя", "Юля", "Оля"]))
print(random_passwrd(length=12))

list1 = [{"name": return_random_word(arr_words=["Аня", "Надя", "Катя", "Юля", "Оля"])} for x in range(1, 100)]
print(list1)
list1.sort(reverse=False, key=lambda dictionary: dictionary["name"])
print(list1)

########################################################################################################################

########################################################################################################################
# TODO tuple comprehension

# новый массив с квадратами значений другого
list1 = [1, 2, 3, 4, 5]
list2 = []
for i in list1:
    if i % 2 != 0:
        result = i ** 2
        list2.append(result)
tuple1 = tuple(list2)
print(tuple1)

# простейший пример
tuple2 = (i ** 2 for i in [1, 2, 3, 4, 5] if i % 2 != 0)  # <generator object <gen expr> at 0x0000015564F423B0>
print(tuple(tuple2))
########################################################################################################################

########################################################################################################################
# TODO dict comprehension

# новый словарь из пар значений
list10 = [["key_1", 1], ["key_2", 2], ["key_3", 3]]
dict1 = {}
for k, v in list10:
    dict1[k] = v
print(dict1)

# простейший пример
list11 = [["key_1", 1], ["key_2", 2], ["key_3", 3]]
dict2 = {k: v for k, v in list11}
print(dict2)

########################################################################################################################
