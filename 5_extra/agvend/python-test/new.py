
"""
========================= python ==================
У нас есть текстовый файл input.txt. В нем через запятую записаны числа. Надо
написать скрипт который
- создаст output.txt
- запишет в файл суммы чисел сгруппированный по две строки. т.е. сложить все числа
по паре строк
- первая строчка = сумма всех чисел из 1 и 2 строки
- вторая строчка = сумма всех чисел из 3 и 4 строки
- файл можно считать чистым, только целые числа и запятые
- в файле произвольное кол-во строк.
- сумма всех чисел input.txt = сумма всех чисел output.txt
input.txt
5,5,0
5
1,1
1,1
3
4
ожидаемый output.txt
15
4
7
"""
import datetime

def get_data(input_filename: str) -> [list[int], int]:

    _external_sum = 0
    with open(input_filename, mode="r") as file:
        lines = file.readlines()

        # Делим исходный массив построчно по 2 элемента в каждом
        _stack = []
        while len(lines) > 1:
            _stack.append([lines.pop(), lines.pop()])
        if len(_stack):
            _stack = _stack[::-1]

        for _row in _stack:
            _acc = 0
            for _el in _row:
                try:
                    for num in str(_el).strip().split(","):
                        _acc += int(num)
                        _external_sum += int(num)
                except:
                    _acc += 0
            _stack_res.append(_acc)
        return _stack

_stack_res: list[int] = [get_data(input_filename="input1.txt"),

with open("output.txt", mode="w") as file:
    for row in _stack_res:
        file.write(f"{row}\n")
