class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Greedy Approach:
        - Track the farthest index we can reach.
        - If we reach or pass the last index, return True.
        - If at any point we can't move forward, return False.
        """

        reach = 0  # Farthest index we can reach

        for i in range(len(nums)):
            if i > reach:
                return False  # Stuck before this position
            reach = max(reach, i + nums[i])  # Update furthest reach

        return True  # Able to reach end