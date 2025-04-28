class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach:
        - Use backtracking to explore all possible combinations.
        - At each step, we can either:
            1. Choose the current number again (because reuse is allowed).
            2. Move to the next number.
        - Stop if the total exceeds the target or we've checked all candidates.
        - When total equals the target, record the current combination.
        """

        res = []  # To store all valid combinations

        def backtrack(i, cur, total):
            # Base case: valid combination found
            if total == target:
                res.append(cur[:])  # Append a copy of current combination
                return

            # Base case: stop exploring if out of bounds or total exceeds target
            if i >= len(candidates) or total > target:
                return

            # Option 1: Include candidates[i] and stay on same index (can reuse)
            cur.append(candidates[i])
            backtrack(i, cur, total + candidates[i])
            cur.pop()  # Backtrack to explore other options

            # Option 2: Skip candidates[i] and move to the next
            backtrack(i + 1, cur, total)

        # Start backtracking from index 0, empty combination, and sum 0
        backtrack(0, [], 0)
        return res