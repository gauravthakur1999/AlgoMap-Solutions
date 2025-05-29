class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Approach:
        - Use dynamic programming with a 2D table.
        - dp[i][j] = length of LCS between text1[0..i-1] and text2[0..j-1]
        - If characters match, extend LCS: dp[i][j] = 1 + dp[i-1][j-1]
        - Else, take the maximum by skipping a character from either string.
        """

        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    # Characters match → extend LCS
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    # Characters don't match → skip one from either string
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]  # Bottom-right cell contains final answer
