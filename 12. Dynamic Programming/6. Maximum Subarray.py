class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Approach:
        - Use dynamic programming to find the maximum subarray sum ending at each index.
        - Let dp[i] represent the maximum sum of a subarray ending at index i.
        - At each step, you can either:
            - Start a new subarray at index i (just nums[i]), or
            - Extend the previous subarray (dp[i-1] + nums[i])
        - So: dp[i] = max(nums[i], dp[i-1] + nums[i])
        - Track the overall maximum while building the dp array.

        Time: O(n)
        Space: O(n) (can be optimized to O(1))
        """

        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]  # base case: best subarray ending at index 0 is nums[0]
        max_sum = dp[0]  # overall maximum

        for i in range(1, n):
            # Either start new subarray at i, or extend previous one
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            max_sum = max(max_sum, dp[i])  # update global max if needed

        return max_sum
        