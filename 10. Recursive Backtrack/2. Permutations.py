class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Approach:
        - Use backtracking to generate all permutations.
        - At each step, choose an unused number and add it to the current path.
        - Once the path length equals nums length, we have a complete permutation.
        """

        res = []      # Final result list to store permutations
        used = set()  # Track which numbers are already used

        def backtrack(path):
            # Base case: if path is full, add to result
            if len(path) == len(nums):
                res.append(path[:])  # Make a copy before appending
                return

            # Try all unused numbers
            for num in nums:
                if num in used:
                    continue  # Skip already used numbers

                # Choose
                path.append(num)
                used.add(num)

                # Explore
                backtrack(path)

                # Undo (backtrack)
                path.pop()
                used.remove(num)

        backtrack([])
        return res