########################################################################################################################
# TODO цикл по итераторам for

list_val1 = [1, 2, 3, 4, 5, 6]
for i in list_val1:
    print(i)

for j in "Python":
    print(j)

for i in range(1, 100, 1):
    print(i)

for i in range(1, 100, 1):
    print(i)
    for j in "Python":
        print(str(i) + " | " + j)

# сумма всех нечётных чисел до 100
summator = 0
for i in range(1, 10):
    if i % 2 == 0:
        summator = summator + i
    else:
        print("Число нечётное, не добавляем")
print(summator)

for j in range(1, 5000):
    if j % 2 != 0:
        continue  # пропускает эту итерацию цикла

    if j >= 50:
        break  # останавливает цикл

    print(j)


value7 = {
    "key_1": "value_1",
    "key_2": 10,
    "key_3": True
}

for key, value in value7.items():  # (key, value) #
    print(f"{key}:  {value} type - {type(value)}")
!
########################################################################################################################

########################################################################################################################
# TODO условный цикл (с предусловием / с постусловием) while / do while

index = 1
while index <= 10:
    print(index)
    index = index + 1

# бесконечный цикл!
# while True:
#     print("Hello")

i = 0
while True:
    i = i + 1
    if i <= 3:
        continue  # пропускает эту итерацию цикла
    elif i >= 7:
        break  # останавливает цикл
    print(i)

########################################################################################################################
