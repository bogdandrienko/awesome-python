########################################################################################################################
# TODO MFTI

# TODO каскадное присваивание
a1 = b1 = c1 = 12  # все "переменные" имеют ссылку на один объект
print(a1, b1, c1)

# TODO множественное присваивание
a2, b2, c2 = 1, 2, 3  # все "переменные" имеют ссылку на один объект
# tuple(a2, b2, c2) = tuple(1, 2, 3)
print(a2, b2, c2)

# TODO смена ссылок
x1 = 12
print(x1)
x1 = 13  # имя переменной начинает ссылаться на другой объект,
# предыдущий объект остаётся прежним (т.к. integer неизменяемый тип) и без ссылки "убивается" сборщиком мусора
print(x1)

# TODO обмен переменных
a3 = 12
b3 = 13
print(a3, b3)
a3, b3 = b3, a3
print(a3, b3)

# TODO "множественное" возведение в степень
#        2    1
a4 = 12 ** 3 ** 2

# TODO else в цикле while
index = 1
while index < 10:
    print(index)
    index += 1
else:
    # блок только если цикл успешно завершён (без break)
    print(index)

########################################################################################################################

########################################################################################################################
# TODO EXTRA


# Итераторы
mylist = [1, 2, 3]
for i in mylist:
    print(i)

mylist = [x * x for x in range(3)]
for i in mylist:
    print(i)

# Это удобно, потому что можно считывать из них значения сколько потребуется —
# однако все значения хранятся в памяти, а это не всегда желательно, если у вас много значений.

# Генераторы
mygenerator = (x * x for x in range(3))
for i in mygenerator:
    print(i)


# Генераторы это тоже итерируемые объекты, но прочитать их можно лишь один раз. Это связано с тем,
# что они не хранят значения в памяти, а генерируют их на лету

# Yield это ключевое слово, которое используется примерно как return — отличие в том,
# что функция вернёт генератор

def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i * i


mygenerator = createGenerator()  # создаём генератор
print(mygenerator)  # mygenerator является объектом!
for i in mygenerator:
    print(i)

# корутины

import asyncio


async def count_to_three():
    print("Веду отсчёт. 1")
    await asyncio.sleep(0)
    print("Веду отсчёт. 2")
    await asyncio.sleep(0)
    print("Веду отсчёт. 3")
    await asyncio.sleep(0)


coroutine_counter = count_to_three()
print(coroutine_counter)  # <coroutine object count_to_three at 0x7f5a58486a98>
coroutine_counter.send(None)  # Выведет "Веду отсчёт. 1"
coroutine_counter.send(None)  # Выведет "Веду отсчёт. 2"
coroutine_counter.send(None)  # Выведет "Веду отсчёт. 3"
coroutine_counter.send(None)  # Выбросит ошибку StopIteration

############################################
# виртуальное окружение и наследование глобальных пакетов
# virtualenv --system-site-packages mycoolproject
############################################

#########################################
# запуск скрипта
# python -m pdb my_script.py
#########################################

############################################
# генераторы
from contextlib import contextmanager


@contextmanager
def open_file(name):
    f = open(name, 'w')
    yield f
    f.close()


###############################################

############################################
# else в циклах
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n / x)
            break
    else:
        # Цикл не нашел целочисленного делителя для n
        print(n, 'is a prime number')
########################################

####################################
# отладчик python
import pdb


def make_bread():
    pdb.set_trace()
    return "У меня нет времени"


print(make_bread())
######################################

###########################################
# тернарные операторы
is_nice = True
state = "nice" if is_nice else "not nice"


############################################

#######################################################
# распаковка
def profile():
    name = "Danny"
    age = 30
    return name, age


profile_name, profile_age = profile()
print(profile_name)
# Вывод: Danny

print(profile_age)


# Вывод: 30
#####################################################


###########################################################
# магические переменные *args и **kwargs
def test_var_args(f_arg, *argv):
    print("Первый позиционный аргумент:", f_arg)
    for arg in argv:
        print("Другой аргумент из *argv:", arg)


test_var_args('yasoob', 'python', 'eggs', 'test')


def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


greet_me(name="yasoob")
###########################################################

######################################################
# enumerate
my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)

# Вывод:
# 1 apple
# 2 banana
# 3 grapes
# 4 pear


my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list, 1))
print(counter_list)
# Вывод: [(1, 'apple'), (2, 'banana'), (3, 'grapes'), (4, 'pear')]
####################################################

###################################################
# map
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, items))


def multiply(x):
    return (x * x)


def add(x):
    return (x + x)


funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

# Вывод:
# [0, 0]
# [1, 2]
# [4, 4]
# [9, 6]
# [16, 8]
####################################################

####################################################
# filter
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# Вывод: [-5, -4, -3, -2, -1]
######################################################

######################################################
#
product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num

# product = 24


from functools import reduce

product = reduce((lambda x, y: x * y), [1, 2, 3, 4])


# Вывод: 24
##################################################

##################################################
# generator
def generator_function():
    for i in range(10):
        yield i


for item in generator_function():
    print(item)


# Вывод: 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
##################################################

###################################################
# корутины
def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)


search = grep('coroutine')
next(search)
# Вывод: Searching for coroutine
search.send("I love you")
search.send("Don't you love me?")
search.send("I love coroutines instead!")
# Вывод: I love coroutines instead!

########################################################################################################################
