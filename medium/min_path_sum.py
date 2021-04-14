#
# @param matrix int整型二维数组 the matrix
# @return int整型
#
class Solution:
    def minPathSum(self, matrix):
        row, col = len(matrix), len(matrix[0])
        dp = [[0] * col for _ in range(row)]

        dp[0][0] = matrix[0][0]
        for i in range(1, row):
            dp[i][0] = dp[i - 1][0] + matrix[i][0]
        for j in range(1, col):
            dp[0][j] = dp[0][j - 1] + matrix[0][j]

        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]
        return dp[-1][-1]
