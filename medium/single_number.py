from typing import List


def singleNumber(nums: List[int]) -> int:
    for i, n in enumerate(nums):
        if nums.count(n) == 1:
            return n
    return -1


def singleNumber(nums: List[int]) -> int:
    num_map = {}
    for n in nums:
        if n in num_map:
            num_map[n] += 1
        else:
            num_map[n] = 1
    for k, v in num_map.items():
        if v == 1:
            return k
    return -1


def singleNumber(nums: List[int]) -> int:
    ones, twos = 0, 0
    for num in nums:
        ones = ones ^ num & ~twos
        twos = twos ^ num & ~ones
    return ones
