import math


def calc(number1, number2, operation="-"):
    # print(number1, number2, operation)
    if operation == "+":
        return number1 + number2
    if operation == "-":
        return number1 - number2
    if operation == "*":
        return number1 * number2
    if operation == "/":
        if number2 == 0:
            print("Второе число не может быть 0")
        else:
            return number1 / number2
    if operation == "**":
        return number1 ** number2
    if operation == "//":
        if number2 == 0:
            print("Второе число не может быть 0")
        else:
            return number1 // number2
    if operation == "sqrt":
        return math.sqrt(number1)
    if operation == "%":
        if number2 == 0:
            print("Второе число не может быть 0")
        else:
            return number1 % number2


# pass - пропуск строки

# num1 = int(input("Введите первое число:"))
# num2 = int(input("Введите второе число:"))
# oper = str(input("Введите операцию:"))
# result = calc(num1, num2, oper)
result = calc(10, 20)
print(result)

result1 = calc(operation="/", number1=10, number2=2)
print(result1)


def calc_3(number1, number2, operation="-"):
    # print(number1, number2, operation)
    if operation == "+":
        return number1 + number2
    if operation == "-":
        return number1 - number2
    if operation == "*":
        return number1 * number2
    if operation == "/":
        if number2 == 0:
            print("Второе число не может быть 0")
        else:
            return number1 / number2
    if operation == "**":
        return number1 ** number2
    if operation == "//":
        if number2 == 0:
            print("Второе число не может быть 0")
        else:
            return number1 // number2
    if operation == "sqrt":
        return math.sqrt(number1)
    if operation == "%":
        if number2 == 0:
            print("Второе число не может быть 0")
        else:
            return number1 % number2

class Calc:
    def __init__(self, value1: float, value2: float):
        self.value1 = value1
        self.value2 = value2

        self.sum = value1 + value2

    def sum(self):
        return self.sum

    def multiply(self):
        return self.value1 * self.value2

    @staticmethod
    def static_multiply(value1, value2):
        return value1 * value2


obj = Calc(12, 1.5)  # __init__
print(obj.multiply())  # multiply

print(Calc.static_multiply(1.5, 20))