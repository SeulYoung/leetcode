from typing import List


class Solution:
    def __init__(self):
        self.max_value, self.value = 0, 0

    def maxValue(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i < row and j < col:
                self.value += grid[i][j]
                if i == row - 1 and j == col - 1 and self.value > self.max_value:
                    self.max_value = self.value

                dfs(i, j + 1)
                dfs(i + 1, j)
                self.value -= grid[i][j]

        row, col = len(grid), len(grid[0])
        dfs(0, 0)
        return self.max_value

    def maxValue(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += max(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]

    def maxValue(self, grid: List[List[int]]) -> int:
        for i in range(1, len(grid)):
            grid[i][0] += grid[i - 1][0]

        for j in range(1, len(grid[0])):
            grid[0][j] += grid[0][j - 1]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] += max(grid[i - 1][j], grid[i][j - 1])
                
        return grid[-1][-1]
