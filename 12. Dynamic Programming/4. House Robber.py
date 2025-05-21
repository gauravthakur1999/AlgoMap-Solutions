class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Approach:
        - Use dynamic programming to track the maximum money that can be robbed.
        - rob1 stores max amount if we skip current house (i-2)
        - rob2 stores max amount including/excluding previous house (i-1)
        - At each step, decide:
            - Rob current house: rob1 + current value
            - Skip current house: rob2
        - Update rob1 and rob2 for the next house.
        - Final answer will be in rob2.
        """

        rob1, rob2 = 0, 0

        for n in nums:
            # Option 1: rob current house → rob1 + n
            # Option 2: skip current house → rob2
            temp = max(n + rob1, rob2)

            # Move window forward
            rob1 = rob2
            rob2 = temp

        return rob2 