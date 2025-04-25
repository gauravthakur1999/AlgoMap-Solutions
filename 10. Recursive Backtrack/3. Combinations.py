class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, path):
            # Base case: if path has k elements, add it to the result
            if len(path) == k:
                res.append(path[:])  # Make a copy
                return
            
            # Try each number starting from 'start' up to n
            for i in range(start, n + 1):
                path.append(i)          # Choose
                backtrack(i + 1, path)   # Explore
                path.pop()               # Unchoose (backtrack)

        backtrack(1, [])
        return res