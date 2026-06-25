class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        maxLen = 0
        start = 0

        for length in range(1, n + 1):
            for i in range(0, n - length + 1):
                j = length + i - 1

                if(s[i] == s[j]):
                    if(length <= 3):
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                if(dp[i][j] and length > maxLen):
                    maxLen = length
                    start = i

        return s[start : start + maxLen]