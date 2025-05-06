class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Approach:
        - Traverse the grid.
        - On each unvisited land cell (1), perform DFS to calculate area.
        - Track and return the maximum area found.
        """

        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            # Base case: out of bounds or water or already visited
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == 0 or
                (r, c) in visited
            ):
                return 0

            visited.add((r, c))
            area = 1  # Current land cell

            # Explore 4 directions
            area += dfs(r+1, c)
            area += dfs(r-1, c)
            area += dfs(r, c+1)
            area += dfs(r, c-1)

            return area

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, dfs(r, c))

        return max_area