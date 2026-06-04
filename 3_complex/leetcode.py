
def twoSum_1(self, nums: list[int], target: int) -> list[int]:
    """
    Задача: хэш
    Сохраняем все индексы чисел в словарь, вычисляем разницу и находим её.
    """
    _res = []
    _val_idx = {} # value: index
    for idx, num in enumerate(nums, 0):
        _diff = target - num
        if _diff in _val_idx:
            return [idx, _val_idx[_diff]]
        _val_idx[num] = idx
    return _res


def isPalindrome_9(self, x: int) -> bool:
    """
    Задача: палиндром
    Превращаем в строку и поворачиваем
    """
    return str(x) == str(x)[::-1]

def longestCommonPrefix_14(self, strs: list[str]) -> str:
    """
    Задача: строки
    Ищем одинаковый префикс посредством отрезания в цикле по одной букве от первого. Если метод поиска подстроки не находит.
    """
    if not strs:
        return ""
    _first_word = strs[0]
    for word in strs[1::]:
        while word.find(_first_word) != 0:
            _first_word = _first_word[:-1:]
    return _first_word





def isValid_20(self, s: str) -> bool:
    """
    Задача: валидность
    Сохраняем в словарь закрывающие скобки. Сохраняем в стек элементы строки, если их нет в словаре, т.е. она открылась,
    но ещё не закрылась. Если она открылась, но её нет в стеке, то значит закрылась неправильно. Берём последний
    элемент от массива и если его нет в словаре, то тоже неправильно.
    """
    if not s:
        return True
    _back_hash = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    _arr = []
    for char in s:
        if char in _back_hash:
            if not _arr:
                return False
            last_ch = _arr.pop(-1)
            if last_ch != _back_hash[char]:
                return False
        else:
            _arr.append(char)
    return len(_arr) == 0

class Solution_21:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def mergeTwoLists_21(self, list1: any[list], list2: any[list]) -> any[list]:
        """
        Задача: связные списки
        Нужно в один связный список составить элементы объектами друг за другом по возрастанию.
        Начиная с нуля, перебираем связные списки, если значение в первом меньше, то берём его и в первом связном списке делаем шаг вперёд.
        Если значение больше во втором, то там делаем шаг вперёд. И до конца нанизываем их друг на друга.
        Если один из связных списков закончился, то проверяем какой свободен и докидываем в конец.
        """
        _res = Solution_21.ListNode()
        _end = _res
        while list1 and list2:
            if list1.val < list2.val:
                _end.next = list1
                list1 = list1.next
            else:
                _end.next = list2
                list2 = list2.next
            _end = _end.next
        if list1:
            _end.next = list1
        if list2:
            _end.next = list2
        return _res.next

def removeDuplicates_26(self, nums: list[int]) -> int:
    """
    Задача: указатели
    Перебираем по длине массива со второго элемента, если текущий элемент не равен предыдущему,
    то записываем его в позицию указателя и шагаем дальше.
    """
    k = 1
    for i in range(1, len(nums)):
        # print(i, k, nums)
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
    # print(k, nums)
    return k

def removeElement_27(self, nums: list[int], val: int) -> int:
    """
    Задача: указатели
    Нужно сэкономить ОЗУ, не создавая новые объекты переместить все числа отличные от целевого в начало.
    Создаём нулевой указатель и перебираем массив, если текущее значение в массиве не целевое,
    то устанавливаем в указатель текущее значение и делаем шаг вперёд указателем.
    """
    k = 0
    for i in range(0, len(nums)):
        # print(i, k, nums)
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    # print(i, k, nums)
    return k



class Solution_243:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    def isPalindrome_243(self, head: any[ListNode]) -> bool:
        """
        Задача: связный список и палиндром
        Нужно проверить что связный список является палиндромом.
        """

        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        # print(stack)
        return stack == stack[::-1]

        self.front = head
        self.back = head
        def recurse(tail: Optional[ListNode]) -> bool:
            # print('\n', self.front, "===", tail)
            if not tail:
                return True
            if not recurse(tail.next):
                return False
            if self.front.val != tail.val:
                return False
            self.front = self.front.next
            return True
        return recurse(self.back)


class Solution_704:
    def search_704(self, nums: list[int], target: int) -> int:
        """
        Задача: бинарный поиск
        Нужно найти число перебирая отсорированный массив.
        """
        # for idx, i in enumerate(nums, 0):
        #     if i == target:
        #         print(idx, i)
        #         return idx
        # return -1
        _left = 0
        _right = len(nums) - 1
        while _left <= _right:
            _middle = (_left + _right) // 2
            _val = nums[_middle]
            # print(_left, _right, _middle, _val)
            if _val == target:
                return _middle
            if _val < target:
                _left = _middle + 1
            else:
                _right = _middle - 1
        return -1


def lengthOfLastWord_58(self, s: str) -> int:
    """
    Задача: строки
    Нужно очистить строку от боковых пробелов и посчитать количество символов до пробела внутреннего.
    """
    # words = s.strip().split()
    # return len(words[-1])

    _clean_str = s.strip()
    cnt = 0
    for i in _clean_str[::-1]:
        if i == " ":
            return cnt
        cnt += 1
    return cnt


def searchInsert_35(self, nums: list[int], target: int) -> int:
    """
    Задача: бинарный поиск
    Нужно найти число перебирая отсорированный массив. Если числа нет, вернуть индекс где оно должно было бы быть.
    """
    _left = 0
    _right = len(nums) - 1
    while _left <= _right:
        _mid = (_left + _right) // 2
        _val = nums[_mid]
        if _val == target:
            return _mid
        if _val < target:
            _left = _mid + 1
        else:
            _right = _mid - 1
    if nums[_mid] < target:
        return _mid + 1
    else:
        return _mid

def strStr_28(self, haystack: str, needle: str) -> int:
    """
    Задача: строки
    Нужно найти одну строку в другой или вернуть -1.
    """
    return haystack.find(needle)



def plusOne_66(self, digits: list[int]) -> list[int]:
    """
    Задача: строки
    Нужно массив чисел увеличить на 1 и вернуть в таком же формате.
    """
    _str = "".join([str(x) for x in digits])
    # print(_str)
    _int = int(_str) + 1
    # print(_int)
    _arr = [int(x) for x in str(_int)]
    # print(_arr)
    return _arr

def romanToInt_13(self, s: str) -> int:
    """
    Задача: числа
    Нужно массив букв латинских через словарь превратить в число, но есть нюанс с приставкой.
    """
    _hash = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    _sum = 0
    for i in range(0, len(s)):
        is_not_end = i + 1 < len(s)
        _cur = _hash[s[i]]
        # print('\n', _cur)
        if is_not_end and _cur < _hash[s[i + 1]]:
            _next = _hash[s[i + 1]]
            # print(_next)
            _sum -= _cur
        else:
            _sum += _cur
    return _sum

def mySqrt_69(self, x: int) -> int:
    """
    Задача: бинарный поиск
    Нужно найти минимальное целое число, из которого получается квадрат целевого значения.
    """
    if x < 1:
        return x
    _left = 0
    _right = x
    while _left <= _right:
        _mid = (_left + _right) // 2
        if _mid * _mid == x:
            return _mid
        if _mid * _mid < x:
            _left = _mid + 1
        else:
            _right = _mid - 1
    return _right
