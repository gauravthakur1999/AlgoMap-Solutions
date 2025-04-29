class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Approach:
        - Use a digit-to-letter mapping (like a phone keypad).
        - Use backtracking to build all possible combinations.
        - At each step, pick one letter for the current digit and move to the next.
        - If all digits are used, add the combination to the result.
        """

        if not digits:
            return []

        # Phone keypad mapping
        digit_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        res = []

        def backtrack(i, path):
            if i == len(digits):
                res.append("".join(path))
                return

            letters = digit_map[digits[i]]
            for letter in letters:
                path.append(letter)
                backtrack(i + 1, path)
                path.pop()  # backtrack

        backtrack(0, [])
        return res