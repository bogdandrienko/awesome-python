def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    return str(x) == str(x)[::-1]

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i_idx, i in enumerate(nums, 0):
        for j_idx, j in enumerate(nums, 0):
            if i_idx == j_idx:
                continue
            if i + j == target:
                return [i_idx, j_idx]

    print(twoSum([3,2,4], 6))

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    _first_word = strs[0]
    for word in strs[1::]:
        while word.find(_first_word) != 0:
            _first_word = _first_word[:-1:]
            if len(_first_word) == 0:
                return ""
    return _first_word

    print(longestCommonPrefix(["flower", "flow", "flight"]))
    print(longestCommonPrefix(["dog","racecar","car"]))


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    _hash_map = {
        "(": ")",
        "{": "}",
        "[": "]",
        ")": "(",
        "}": "{",
        "]": "[",
    }
    _pred = ""
    for char in s:
        print(s)
    return True
print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("([])"))
print(isValid("(]"))
