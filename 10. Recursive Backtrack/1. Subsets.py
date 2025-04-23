class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Approach:
        - Use Depth-First Search (DFS) + Backtracking to explore all possible subsets.
        - At each index, we have two choices:
            1. Include the current element in the subset.
            2. Exclude the current element and move on.
        - This creates a binary decision tree of inclusion/exclusion for each element.
        - Once we reach the end of the array (i >= len(nums)), we record the current subset.
        """

        res = []         # This will store all subsets
        subset = []      # Current subset being built

        # Recursive function to explore all subset options
        def dfs(i):
            # Base case: we've considered all elements
            if i >= len(nums):
                res.append(subset.copy())  # Save a copy of the current subset
                return

            # Decision 1: Include nums[i] in the subset
            subset.append(nums[i])
            dfs(i + 1)

            # Decision 2: Exclude nums[i] from the subset (backtrack)
            subset.pop()
            dfs(i + 1)

        # Start the recursion from index 0
        dfs(0)
        return res