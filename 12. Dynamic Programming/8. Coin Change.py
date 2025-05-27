class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Approach:
        - Use dynamic programming to build a solution from amount 0 to target amount.
        - dp[a] will store the minimum number of coins needed to make amount 'a'.
        - Initialize dp[0] = 0 (0 coins to make 0), and the rest as a large number (amount + 1).
        - For each amount from 1 to 'amount', try every coin:
            - If coin can contribute (a - c >= 0), update dp[a] = min(dp[a], 1 + dp[a - c])
        - Return dp[amount] if it's not the initialized max value; else return -1.
        """

        # Step 1: Initialize DP array
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # base case: 0 coins needed to make 0

        # Step 2: Build the DP table
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        # Step 3: Final answer
        return dp[amount] if dp[amount] != amount + 1 else -1