class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Approach:
        - Reverse the water flow: simulate from oceans inward.
        - DFS from all border cells touching Pacific & Atlantic.
        - Track cells reachable by each ocean.
        - Return cells that are reachable by both.
        """

        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, visited, prev_height):
            # Out of bounds or already visited or invalid flow
            if (
                r < 0 or c < 0 or r >= rows or c >= cols or
                (r, c) in visited or
                heights[r][c] < prev_height
            ):
                return

            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])

        # Step 1: DFS from Pacific Ocean (top and left edges)
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])         # Left edge
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])  # Right edge

        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])         # Top edge
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])  # Bottom edge

        # Step 2: Intersection of cells reachable by both oceans
        res = []
        for r in range(rows):
            for c in range(cols):
                if ((r, c) in pacific and (r, c) in atlantic):
                    res.append((r,c))
        return res