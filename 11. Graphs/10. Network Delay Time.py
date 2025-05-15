class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Approach:
        - Use Dijkstra's algorithm to find shortest times from node k to all others.
        - Use a min-heap to always process the next node with the shortest known delay.
        - Track visited nodes to avoid processing a node more than once.
        """

        # Step 1: Build the graph
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))  # u -> v with weight w

        # Step 2: Min-heap for (time, node)
        min_heap = [(0, k)]  # Start with time 0 from node k
        visited = {}         # node: time it was first reached

        while min_heap:
            time, node = heapq.heappop(min_heap)

            if node in visited:
                continue  # We've already processed this node

            visited[node] = time  # Record shortest time to this node

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (time + weight, neighbor))

        # Step 3: Check if all nodes were visited
        if len(visited) != n:
            return -1

        return max(visited.values())  # Time when the last node gets the signal
