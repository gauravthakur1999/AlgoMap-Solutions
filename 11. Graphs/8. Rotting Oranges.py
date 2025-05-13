class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Approach:
        - Use BFS starting from all initially rotten oranges (multi-source).
        - For each minute (level), rot adjacent fresh oranges.
        - Count minutes and track remaining fresh oranges.
        """

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # Step 1: Initialize queue with rotten oranges and count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        minutes = 0

        # Step 2: BFS from all rotten oranges
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2  # Rot it
                        queue.append((nr, nc))
                        fresh -= 1
            minutes += 1

        return minutes if fresh == 0 else -1