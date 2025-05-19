class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Approach:
        - This is a Fibonacci-style DP problem.
        - Let dp[i] represent the number of ways to reach step i.
        - dp[i] = dp[i-1] + dp[i-2]
        - Base cases:
            dp[1] = 1 (only 1 step)
            dp[2] = 2 (1+1 or 2)
        - Use two variables to track last two results (space optimized).
        """

        if n <= 2:
            return n

        first, second = 1, 2  # dp[1], dp[2]

        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third

        return second