class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        Approach:
        - Build an undirected graph using an adjacency list from the edge list.
        - Use Depth-First Search (DFS) starting from the 'start' node.
        - Keep track of visited nodes to prevent revisiting and infinite loops.
        - If we reach the 'end' node during DFS, return True.
        - If we explore all possible paths and don't reach 'end', return False.
        """

        # Step 1: Build adjacency list for the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Step 2: Set to store visited nodes to avoid cycles
        visited = set()

        # Step 3: DFS function to explore the graph
        def dfs(node):
            # If we reach the destination node, return True
            if node == destination:
                return True

            # Mark current node as visited
            visited.add(node)

            # Explore all unvisited neighbors
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True  # Early return if path found

            # No path found from this node
            return False

        # Step 4: Start DFS from the 'start' node
        return dfs(source)