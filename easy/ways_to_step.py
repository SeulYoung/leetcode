class Solution:
    def __init__(self):
        self.count = 0

    def waysToStep(self, n: int) -> int:
        def dfs(n):
            if n == 1:
                self.count += 1
            elif n == 2:
                self.count += 2
            elif n == 3:
                self.count += 4
            else:
                dfs(n - 1)
                dfs(n - 2)
                dfs(n - 3)

        dfs(n)
        return self.count

    def waysToStep(self, n: int) -> int:
        if n < 3:
            return n
        elif n == 3:
            return 4

        dp0, dp1, dp2 = 1, 2, 4
        for _ in range(4, n + 1):
            dp0, dp1, dp2 = dp1, dp2, (dp0 + dp1 + dp2) % 1000000007

        return dp2
