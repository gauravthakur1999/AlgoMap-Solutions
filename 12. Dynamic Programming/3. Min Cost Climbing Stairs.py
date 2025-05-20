class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Approach:
        - Use dynamic programming to compute the min cost to reach each step.
        - Let dp[i] = min cost to reach step i.
        - To reach step i, you can come from:
            - step i-1 with cost[i-1]
            - step i-2 with cost[i-2]
        - You can start at step 0 or 1, so base cases:
            dp[0] = 0
            dp[1] = 0
        - Final answer is dp[n], where n = len(cost)
        """

        n = len(cost)
        prev2, prev1 = 0, 0  # dp[0], dp[1]

        for i in range(2, n + 1):
            curr = min(prev1 + cost[i - 1], prev2 + cost[i - 2])
            prev2, prev1 = prev1, curr

        return prev1