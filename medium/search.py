#
# 如果目标值存在返回下标，否则返回 -1
# @param nums int整型一维数组
# @param target int整型
# @return int整型
#
class Solution:
    def search(self, nums, target):
        begin, end = 0, len(nums) - 1
        while begin < end:
            mid = (begin + end) // 2
            if nums[mid] >= target:
                end = mid
            else:
                begin = mid + 1
        return end if end >= 0 and nums[end] == target else -1
