from typing import List


def swapNumbers(numbers: List[int]) -> List[int]:
    numbers[0] += numbers[1]
    numbers[1] = numbers[0] - numbers[1]
    numbers[0] -= numbers[1]
    return numbers


def swapNumbers(numbers: List[int]) -> List[int]:
    return [numbers[1], numbers[0]]


def swapNumbers(numbers: List[int]) -> List[int]:
    numbers[0] ^= numbers[1]
    numbers[1] ^= numbers[0]
    numbers[0] ^= numbers[1]
    return numbers
