from typing import List


def maxIncreaseKeepingSkyline(grid: List[List[int]]) -> int:
    # row_max = col_max = []
    # print(row_max is col_max)
    # row_max = col_max = list()
    # print(row_max is col_max)

    # 在多目标赋值中，其本质即类似三个变量的指针指向了同一个内存空间，即三个变量共享了内存内同一对象
    # 对于不可变对象来说，在使用这些变量是不存在问题的
    # 在使用多目标赋值时，需要考虑对象本身属性是否为可变对象，否则应该考虑对每个变量名进行单独赋值或者利用浅拷贝、深拷贝
    row_max, col_max = [], []

    h, w = len(grid), len(grid[0])
    for row in grid:
        row_max.append(max(row))
    for j in range(w):
        col_max.append(max(grid[i][j] for i in range(h)))

    max_sum = 0
    for i in range(h):
        for j in range(w):
            max_sum += min(row_max[i], col_max[j]) - grid[i][j]
    return max_sum


def maxIncreaseKeepingSkyline(grid: List[List[int]]) -> int:
    row_max = [max(row) for row in grid]
    col_max = [max(col) for col in zip(*grid)]

    return sum(min(row_max[i], col_max[j]) - grid[i][j]
               for i in range(len(grid))
               for j in range(len(grid[0])))
