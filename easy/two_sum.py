from typing import List


#
# @param numbers int整型一维数组
# @param target int整型
# @return int整型一维数组
#
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return []

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(numbers):
            key = target - num
            if key in hash_map:
                return [hash_map[key] + 1, i + 1]
            hash_map[num] = i
        return []
