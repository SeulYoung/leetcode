#
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def maxLength(self, arr):
        max_length, start = 0, 0
        hash_map = {}
        for i, num in enumerate(arr):
            if num in hash_map:
                # 从重复数字位置加1开始找新的长度
                start = max(start, hash_map[num] + 1)
            hash_map[num] = i
            max_length = max(max_length, i - start + 1)
        return max_length

    def maxLength(self, arr):
        max_length = 0
        num_list = []
        for num in arr:
            if num in num_list:
                num_list = num_list[num_list.index(num) + 1:]
            num_list.append(num)
            max_length = max(max_length, len(num_list))
        return max_length
