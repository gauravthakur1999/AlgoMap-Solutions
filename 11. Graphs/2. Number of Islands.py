class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Approach:
        - Traverse the 2D grid.
        - Every time we find an unvisited land cell ('1'), we perform BFS to
          explore the entire island and mark all its parts as visited.
        - Each BFS call represents discovering one full island.
        - Count how many times we start a BFS — that gives the total number of islands.
        """

        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()  # To track visited land cells
        islands = 0      # Count of islands

        # Perform BFS from a given cell
        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))

            # 4-directional movement: right, down, left, up
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    # Check bounds, cell value, and visited status
                    if (0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] == "1" and
                        (nr, nc) not in visited):
                        queue.append((nr, nc))
                        visited.add((nr, nc))

        # Traverse each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # Start BFS if it's unvisited land
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1  # Found one new island

        return islands