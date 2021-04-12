class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        hash_map = {}
        for num in numbers:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
            if hash_map[num] > len(numbers) / 2:
                return num
        return 0

    def MoreThanHalfNum_Solution(self, numbers):
        numbers.sort()
        num = numbers[len(numbers) // 2]
        if numbers.count(num) > len(numbers) / 2:
            return num
        return 0

    def MoreThanHalfNum_Solution(self, numbers):
        count = 0
        cur = 0
        for num in numbers:
            if count == 0:
                cur = num
                count = 1
            elif cur == num:
                count += 1
            else:
                count -= 1
        return cur if numbers.count(cur) > len(numbers) / 2 else 0
