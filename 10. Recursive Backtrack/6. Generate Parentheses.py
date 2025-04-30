class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Approach:
        - Use backtracking to generate all valid combinations.
        - Track how many open and close parentheses have been placed so far.
        - Only add '(' if open < n.
        - Only add ')' if close < open.
        - When open == close == n, the current string is valid.
        """

        res = []

        def backtrack(current, open_count, close_count):
            # Base case: valid combination formed
            if open_count == close_count == n:
                res.append(current)
                return

            # Add '(' if we haven't used up all opens
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # Add ')' if it won't exceed the number of opens
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return res