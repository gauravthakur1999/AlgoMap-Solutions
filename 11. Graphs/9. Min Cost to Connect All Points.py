class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        Approach:
        - Build a complete graph where each point is connected to every other point.
        - The edge weight is the Manhattan distance between two points.
        - Use Prim's algorithm to construct the Minimum Spanning Tree (MST).
        - Start from any point (e.g., point 0) and always add the smallest edge
          that connects a new point to the MST.
        - Stop when all points are included in the MST.
        """

        N = len(points)

        # Step 1: Build adjacency list with all edge distances
        adj = {i: [] for i in range(N)}  # i -> list of [cost, neighbor]
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                # Since undirected, add both directions
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Step 2: Prim's algorithm
        res = 0  # Total cost of MST
        visit = set()  # Tracks nodes included in MST
        minH = [[0, 0]]  # Start from node 0 with cost 0

        while len(visit) < N:
            cost, node = heapq.heappop(minH)

            if node in visit:
                continue

            visit.add(node)
            res += cost

            # Add all neighbors of this node to the heap
            for neiCost, nei in adj[node]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])

        return res