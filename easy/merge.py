from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp_list = [0] * (m + n)
        i, j, k = 0, 0, 0
        while i < m or j < n:
            if i == m:
                tmp_list[k] = nums2[j]
                j += 1
            elif j == n:
                tmp_list[k] = nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                tmp_list[k] = nums2[j]
                j += 1
            else:
                tmp_list[k] = nums1[i]
                i += 1
            k += 1
        nums1[:] = tmp_list

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # for i in range(n):
        #     nums1[m + i] = nums2[i]
        nums1[m:] = nums2
        nums1.sort()

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2 = m - 1, n - 1
        tail = m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[:tail + 1] = nums2[:p2 + 1]
                break
            elif p2 == -1:
                break
            elif nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1
