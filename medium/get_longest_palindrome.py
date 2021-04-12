class Solution:
    def getLongestPalindrome(self, A, n):
        def is_palindrome(s):
            l = len(s)
            for i in range(l // 2):
                if s[i] != s[l - 1 - i]:
                    return False
            return True

        max_length = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                if is_palindrome(A[i:j]):
                    max_length = max(max_length, j - i)
        return max_length

    def getLongestPalindrome(self, A, n):
        dp = [[False] * n for _ in range(n)]
        max_length = 0
        for l in range(n):
            for i in range(n - l):
                j = i + l
                if l == 0:
                    dp[i][j] = True
                elif l == 1 and A[i] == A[j]:
                    dp[i][j] = True
                elif dp[i + 1][j - 1] and A[i] == A[j]:
                    dp[i][j] = True
                if dp[i][j]:
                    max_length = max(max_length, l + 1)
        return max_length

    def getLongestPalindrome(self, A, n):
        def center_spread(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        max_length = 0
        for i in range(n):
            left, right = center_spread(A, i, i)
            max_length = max(max_length, right - left)
            left, right = center_spread(A, i, i + 1)
            max_length = max(max_length, right - left)
        return max_length + 1
