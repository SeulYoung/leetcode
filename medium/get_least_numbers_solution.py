class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k > len(tinput):
            return []
        tinput.sort()
        return tinput[:k]

    def GetLeastNumbers_Solution(self, tinput, k):
        def quick_sort(num_list, left, right):
            if left < right:
                i, j, num = left, right, num_list[left]
                while i < j:
                    while i < j and num < num_list[j]:
                        j -= 1
                    if i < j:
                        num_list[i] = num_list[j]
                        i += 1

                    while i < j and num > num_list[i]:
                        i += 1
                    if i < j:
                        num_list[j] = num_list[i]
                        j -= 1

                num_list[i] = num
                quick_sort(num_list, left, i - 1)
                quick_sort(num_list, i + 1, right)

        if k > len(tinput):
            return []
        quick_sort(tinput, 0, len(tinput) - 1)
        return tinput[:k]

    def GetLeastNumbers_Solution(self, tinput, k):
        def quick_sort(num_list):
            if not num_list:
                return []

            num = num_list[0]
            left = quick_sort([n for n in num_list[1:] if n < num])
            right = quick_sort([n for n in num_list[1:] if n >= num])
            return left + [num] + right

        if k > len(tinput):
            return []
        tinput = quick_sort(tinput)
        return tinput[:k]

    def GetLeastNumbers_Solution(self, tinput, k):
        def merge_sort(num_list):
            if len(num_list) <= 1:
                return num_list
            mid = len(num_list) // 2
            left = merge_sort(num_list[:mid])
            right = merge_sort(num_list[mid:])
            return merge(left, right)

        def merge(left, right):
            i, j, res = 0, 0, []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            return res + left[i:] + right[j:]

        if k > len(tinput):
            return []
        tinput = merge_sort(tinput)
        return tinput[:k]

    def GetLeastNumbers_Solution(self, tinput, k):
        def bubble_sort(num_list):
            for i in range(len(num_list)):
                for j in range(1, len(num_list) - i):
                    if num_list[j - 1] > num_list[j]:
                        num_list[j - 1], num_list[j] = num_list[j], num_list[j - 1]

        if k > len(tinput):
            return []
        bubble_sort(tinput)
        return tinput[:k]

    def GetLeastNumbers_Solution(self, tinput, k):
        def select_sort(num_list):
            for i in range(len(num_list) - 1):
                small = i
                for j in range(i + 1, len(num_list)):
                    if num_list[small] > num_list[j]:
                        small = j
                num_list[i], num_list[small] = num_list[small], num_list[i]

        if k > len(tinput):
            return []
        select_sort(tinput)
        return tinput[:k]

    def GetLeastNumbers_Solution(self, tinput, k):
        def insert_sort(num_list):
            for i in range(1, len(num_list)):
                tmp = num_list[i]
                j = i
                while j > 0 and tmp < num_list[j - 1]:
                    num_list[j] = num_list[j - 1]
                    j -= 1
                num_list[j] = tmp

        if k > len(tinput):
            return []
        insert_sort(tinput)
        return tinput[:k]

    def GetLeastNumbers_Solution(self, tinput, k):
        def heap_sort(num_list):
            end = len(num_list)
            for i in range(end // 2 - 1, -1, -1):
                adjust_heap(num_list, num_list[i], i, end)

            for i in range(end - 1, 0, -1):
                tmp = num_list[i]
                num_list[i] = num_list[0]
                adjust_heap(num_list, tmp, 0, i)

        def adjust_heap(num_list, tmp, begin, end):
            i, j = begin, begin * 2 + 1
            while j < end:
                if j + 1 < end and num_list[j] < num_list[j + 1]:
                    j += 1
                elif tmp > num_list[j]:
                    break
                else:
                    num_list[i] = num_list[j]
                    i, j = j, j * 2 + 1
            num_list[i] = tmp

        if k > len(tinput):
            return []
        heap_sort(tinput)
        return tinput[:k]
