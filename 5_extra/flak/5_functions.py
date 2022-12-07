# функция без аргументов
import random
from typing import Union
from attr._compat import ordered_dict


def sum1():
    print("Hi")


# sum1()


# функция с позиционными аргументами
def sum2(val1, val2):
    print(val1 + val2)


# sum2(10, 15)


# функция с именнованными аргументами
def sum3(val1, val2):
    print(val1 / val2)


# sum3(val2=2, val1=15)


# функция c аргументом по умолчанию
def sum4(val1, val2=2, val3=None):
    if val3 is None:
        val3 = ["1214"]
    print(val1 / val2)


# sum4(5)


# типизация
def sum5(val1: Union[float, int], val3: Union[list, set, tuple], val2=2) -> float:
    print(val1 / val2)
    return val1 / val2


# sum5(10, [12])

# лямбда функции
sum6 = lambda a, b: (a * b) + 5


# print(sum6(20, 5))

def get_key(item):
    return item.key


# list2 = [[random.randrange(1, 100), random.randrange(1, 100)] for x in range(1, 100)]
# print(list2)
# list2.sort(reverse=False, key=lambda list_item: list_item[1])
# print(list2)

people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}
dict(sorted(people.items()))  # {1: 'Jill', 2: 'Jack', 3: 'Jim', 4: 'Jane'}
print(dict(sorted(people.items(), key=lambda item: item[1])))  # {2: 'Jack', 4: 'Jane', 1: 'Jill', 3: 'Jim'}


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

# my_list = sorted(list1, key=lambda k: k['name'])

# рекурсивная функция
# def factorial_recursive(n):
#     if n == 1:
#         return n
#     return n * factorial_recursive(n-1)
#
# print(factorial_recursive(6))

# def recur(start: int, finish: int) -> int:
#     if start == finish:
#         return start
#     return start + recur(start + 1, finish)
#
#
# print(recur(1, 7))  # 1, 2, 3, 4, 5
