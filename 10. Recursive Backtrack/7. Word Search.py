
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        - Use DFS from each cell that matches word[0].
        - Use a global `visited` set to track visited (r, c) positions.
        - Backtrack by removing (r, c) from visited after exploring.
        """

        rows, cols = len(board), len(board[0])
        visited = set()  # shared set for visited cells

        def dfs(r, c, i):
            # All characters matched
            if i == len(word):
                return True

            # Invalid cell or already visited or character mismatch
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                (r, c) in visited or board[r][c] != word[i]):
                return False

            visited.add((r, c))  # mark current cell as visited

            # Explore all four directions
            found = (dfs(r + 1, c, i + 1) or
                     dfs(r - 1, c, i + 1) or
                     dfs(r, c + 1, i + 1) or
                     dfs(r, c - 1, i + 1))

            visited.remove((r, c))  # backtrack

            return found

        # Try starting DFS from each cell that matches word[0]
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False