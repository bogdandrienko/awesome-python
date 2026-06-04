
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

class Solution21:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def mergeTwoLists(self, list1: any[list], list2: any[list]) -> any[list]:
        """
        Задача: связные списки
        Нужно в один связный список составить элементы объектами друг за другом по возрастанию.
        Начиная с нуля, перебираем связные списки, если значение в первом меньше, то берём его и в первом связном списке делаем шаг вперёд.
        Если значение больше во втором, то там делаем шаг вперёд. И до конца нанизываем их друг на друга.
        Если один из связных списков закончился, то проверяем какой свободен и докидываем в конец.
        """
        _res = Solution21.ListNode()
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



