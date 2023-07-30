"""
https://proglib.io/p/slozhnost-algoritmov-i-operaciy-na-primere-python-2020-11-03
"Сложность алгоритмов и операций на примере Python.html"

«O» большое служит обозначением временной сложности операций алгоритма. Она показывает, сколько времени потребуется
алгоритму для вычисления требуемой операции.
На письме временная сложность алгоритма обозначается как O(n), где n — размер входной коллекции.

O(1)
Обозначение константной временной сложности. Независимо от размера коллекции, время, необходимое для выполнения
операции, константно.

O(log n)
Обозначение логарифмической временной сложности. В этом случае когда размер коллекции увеличивается, время,
необходимое для выполнения операции, логарифмически увеличивается.

O(n)
Обозначение линейной временной сложности. Время, необходимое для выполнения операции, прямо и линейно пропорционально
количеству элементов в коллекции.

O(n log n)
Обозначение квазилинейной временной сложности. Скорость выполнения операции является квазилинейной функцией числа
элементов в коллекции.

O(n^2)
Обозначение квадратичной временной сложности. Время, необходимое для выполнения операции, пропорционально квадрату
элементов в коллекции.

O(n!)
Обозначение факториальной временной сложности. Каждая операция требует вычисления всех перестановок коллекции,
следовательно, требуемое время выполнения операции является факториалом размера входной коллекции.
"""

"""
Благоприятные, средние и худшие случаи
При вычислении временной сложности операции можно получить сложность на основе благоприятного, среднего или худшего 
случая.

Благоприятный случай. Как следует из названия, это сценарий, когда структуры данных и элементы в коллекции вместе с 
параметрами находятся в оптимальном состоянии. Например, мы хотим найти элемент в коллекции. Если этот элемент 
оказывается первым элементом коллекции, то это лучший сценарий для операции.

Средний случай. Определяем сложность на основе распределения значений входных данных.

Худший случай. Структуры данных и элементы в коллекции вместе с параметрами находятся в наиболее неоптимальном 
состоянии. Например, худший случай для операции, которой требуется найти элемент в большой коллекции в виде списка — 
когда искомый элемент находится в самом конце, а алгоритм перебирает коллекцию с самого начала.
"""

"""
Коллекции Python и их временная сложность - 

* Список (list):
Вставка: O(n).
Получение элемента: O(1).
Удаление элемента: O(n).
Проход: O(n).
Получение длины: O(1)

* Множество (set)
Проверить наличие элемента в множестве: O(1).
Отличие множества A от B: O(длина A).
Пересечение множеств A и B: O(минимальная длина A или B).
Объединение множеств A и B: O(N) , где N это длина (A) + длина (B).

* Словарь (dict)
Получение элемента: O(1).
Установка элемента: O(1).
Удаление элемента: O(1).
Проход по словарю: O(n).
"""

"""



"""

########################################################################################################################
# TODO сортировка пузырьком

numbers_orig = [5, 2, 6, 7, 8, 12, 15, 111]


def myBubbleSort(myList):
    for i in range(len(myList) - 1):
        for j in range(len(myList) - i - 1):
            if myList[j] < myList[j + 1]:
                temp = myList[j]
                myList[j] = myList[j + 1]
                myList[j + 1] = temp


print("Original list:")
print(numbers_orig)
myBubbleSort(numbers_orig)
print("Sorted list:")
print(numbers_orig)


########################################################################################################################

########################################################################################################################
# TODO бинарное дерево


class BinaryTree:
    def __init__(self, data: int):
        self.left = None
        self.right = None
        self.root = data

    def get_data(self):
        return self.root

    def insert_new_data(self, data: int):
        if self.root:
            if data < self.root:
                # левый
                if self.left is not None:
                    self.left.insert_new_data(data)
                else:
                    self.left = BinaryTree(data)
                # левый

            elif data > self.root:
                # правый
                if self.right is not None:
                    self.right.insert_new_data(data)
                else:
                    self.right = BinaryTree(data)
                # правый

            else:
                print("Значение повторяется")

        else:
            self.root = data

    def print_all_edges(self):
        print(self.root)
        print(self.left)
        print(self.right)


tree1 = BinaryTree(1)  # создание экземляра класса - создание объекта
tree1.insert_new_data(2)
tree1.insert_new_data(3)
tree1.insert_new_data(9)
tree1.insert_new_data(6)
tree1.insert_new_data(11)
tree1.insert_new_data(15)
print(f"root: {tree1.root}")
print(f"root: {tree1.right.root}")

print(f"root: {tree1.right.right.root}")

print(f"root: {tree1.right.right.right.root}")

print(f"root: {tree1.right.right.right.right.root}")
print(f"root: {tree1.right.right.right.left.root}")

print(f"root: {tree1.right.right.right.right.right.root}")

########################################################################################################################

########################################################################################################################
# TODO шифр Цезаря


class CaesarCipher(object):
    """
    Цезарь шифрование и дешифрование
    """

    def __crypt(self, char, key):
        """
        Зашифровать одну букву, смещение
        @param char: {str} один символ
        @param key: {num} смещение
        @return: {str} зашифрованный символ
        """
        if not char.isalpha():
            return char
        else:
            base = "A" if char.isupper() else "a"
            return chr((ord(char) - ord(base) + key) % 26 + ord(base))

    def encrypt(self, char, key):
        """
        Шифровать персонажей
        """
        return self.__crypt(char, key)

    def decrypt(self, char, key):
        """
        Расшифровать символы
        """
        return self.__crypt(char, -key)

    def __crypt_text(self, func, text, key):
        """
        Зашифровать текст
        @param char: {str} текст
        @param key: {num} смещение
        @return: {str} зашифрованный текст
        """
        lines = []
        for line in text.split("\n"):
            words = []
            for word in line.split(" "):
                chars = []
                for char in word:
                    chars.append(func(char, key))
                words.append("".join(chars))
            lines.append(" ".join(words))
        return "\n".join(lines)

    def encrypt_text(self, text, key):
        """
        Зашифровать текст
        """
        return self.__crypt_text(self.encrypt, text, key)

    def decrypt_text(self, text, key):
        """
        Расшифровать текст
        """
        return self.__crypt_text(self.decrypt, text, key)


plain = """
you know? I love you!
"""
key = 3

cipher = CaesarCipher()

# Шифрование
print(cipher.encrypt_text(plain, key))
# brx nqrz? L oryh brx!

# Расшифровать
print(cipher.decrypt_text("brx nqrz? L oryh brx!", key))


# you know? I love you!

########################################################################################################################
