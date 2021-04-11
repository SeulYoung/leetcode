class Solution:
    def Fibonacci(self, n):
        def dfs(n):
            if n <= 1:
                return n
            else:
                return dfs(n - 1) + dfs(n - 2)

        return dfs(n)

    def Fibonacci(self, n):
        dp = [0, 1] + [0] * (n - 1)
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def Fibonacci(self, n):
        if n <= 1:
            return n
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b
