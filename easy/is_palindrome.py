def isPalindrome(x: int) -> bool:
    if x < 0:
        return False

    str_x = str(x)
    mid = len(str_x) // 2
    left = str_x[:mid]
    if len(str_x) % 2 == 0:
        mid -= 1
    right = str_x[:mid:-1]
    return True if left == right else False


def isPalindrome(x: int) -> bool:
    if x < 0:
        return False

    str_x = str(x)
    return True if str_x == str_x[::-1] else False


def isPalindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    rev = 0
    while x > rev:
        rev = rev * 10 + x % 10
        x //= 10
    return True if x == rev or x == rev // 10 else False
