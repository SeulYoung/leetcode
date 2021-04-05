class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [5, 4, 3, 2, 1]
        for _ in range(2, n + 1):
            for i in range(3, -1, -1):
                dp[i] += dp[i + 1]
        return dp[0]
