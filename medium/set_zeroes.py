from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    row = col = set()
    h, w = len(matrix), len(matrix[0])
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 0:
                row.add(i)
                col.add(j)

    for i in range(h):
        if i in row:
            matrix[i] = [0] * w
        else:
            for j in col:
                matrix[i][j] = 0


def setZeroes(matrix: List[List[int]]) -> None:
    flag_col0 = False
    h, w = len(matrix), len(matrix[0])

    for i in range(h):
        if matrix[i][0] == 0:
            flag_col0 = True
        for j in range(1, w):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0

    for i in range(1, h + 1):
        k = i % h
        if matrix[k][0] == 0:
            matrix[k] = [0] * w
        else:
            for j in range(1, w):
                if matrix[0][j] == 0:
                    matrix[k][j] = 0
        if flag_col0:
            matrix[k][0] = 0


def setZeroes(matrix: List[List[int]]) -> None:
    flag_col0 = False
    h, w = len(matrix), len(matrix[0])

    for i in range(h):
        if matrix[i][0] == 0:
            flag_col0 = True
        for j in range(1, w):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0

    for i in range(h - 1, -1, -1):
        if matrix[i][0] == 0:
            matrix[i] = [0] * w
        else:
            for j in range(1, w):
                if matrix[0][j] == 0:
                    matrix[i][j] = 0
        if flag_col0:
            matrix[i][0] = 0
