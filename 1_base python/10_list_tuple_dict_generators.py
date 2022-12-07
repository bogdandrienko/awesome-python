fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
# print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
# print(newlist)

list1 = [" apple ", " banana ", " cherry ", "kiwi ", " mango"]
list2 = [str(char).strip() for char in list1 if "i" in char and len(str(char).strip()) > 3]
print(list2)

list3 = [str(x).strip() for x in "Яблоко, банан, груша       , киви      ".split(",")]
print(list3)


!


########################################################################################################################
# TODO list complehension

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
########################################################################################################################

########################################################################################################################
# TODO tuple complehension

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
tuple2 = (i ** 2 for i in [1, 2, 3, 4, 5] if i % 2 != 0)  # <generator object <genexpr> at 0x0000015564F423B0>
print(tuple(tuple2))
########################################################################################################################

########################################################################################################################
# TODO dict complehension

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
