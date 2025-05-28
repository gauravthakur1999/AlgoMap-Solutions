class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Approach:
        - Use dynamic programming.
        - dp[i] represents the length of the longest increasing subsequence ending at index i.
        - Initialize dp[i] = 1 for all i (each element is an LIS of length 1 by itself).
        - For each index i, look back at all previous indices j < i:
            - If nums[j] < nums[i], we can extend the subsequence ending at j to i.
            - So: dp[i] = max(dp[i], dp[j] + 1)
        - Final answer is the max value in dp.
        
        Time: O(n^2)
        Space: O(n)
        """

        dp = [1] * len(nums)  # every element is at least an LIS of 1

        for i in range(len(nums)):
            for j in range(i):  # compare with all elements before i
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)  # the longest of all increasing subsequences