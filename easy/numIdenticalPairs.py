from collections import Counter, defaultdict
from typing import List


def numIdenticalPairs(nums: List[int]) -> int:
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                count += 1
    return count


def numIdenticalPairs(nums: List[int]) -> int:
    m = Counter(nums)
    return sum(v * (v - 1) // 2 for k, v in m.items())


def numIdenticalPairs(nums: List[int]) -> int:
    return sum(nums[i + 1:].count(num) for i, num in enumerate(nums))


def numIdenticalPairs(nums: List[int]) -> int:
    count, hash_map = 0, defaultdict(int)
    for num in nums:
        count += hash_map[num]
        hash_map[num] += 1
    return count
