def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    return str(x) == str(x)[::-1] # превращаем в строку, разворачиваем и проверям
    print(isPalindrome(123))
    print(isPalindrome(121))

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nums_dict = {} # value: index_of_value
    for i_idx, i in enumerate(nums, 0):
        _nedo = target - i # остаток до целевого значения
        if _nedo in nums_dict: # если остаток находится в словаре возвращаем его индекс и текущий индекс
            return [nums_dict[_nedo], i_idx]
        nums_dict[i] = i_idx # запоминаем индекс в массиве каждого значения
    return []
    print(twoSum([3,2,4], 6))

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    _first_word = strs[0] # запоминаем первое число
    for word in strs[1::]:
        while word.find(_first_word) != 0: # идём циклом с конца и отрезаем по одной букве если она не совпадает
            _first_word = _first_word[:-1:]
            if len(_first_word) == 0:
                return ""
    return _first_word # возвращаем остаток
    print(longestCommonPrefix(["flower", "flow", "flight"]))
    print(longestCommonPrefix(["dog","racecar","car"]))

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    _hash_map = {
        ")": "(",
        "}": "{",
        "]": "[",
    } # присваиваем закрывающей скобке отрывающую ключ-значение
    _arr = [] # храним символы
    for char in s:
        if char in _hash_map:
            if not _arr:
                return False
            last_ch = _arr.pop(-1)
            if last_ch != _hash_map[char]:
                return False
        else:
            _arr.append(char)
    return len(_arr) == 0
print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("([])"))
print(isValid("(]"))

