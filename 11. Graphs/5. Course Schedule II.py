class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Approach:
        - Build a graph (adjacency list) and track in-degrees.
        - Start with nodes that have in-degree 0 (no prerequisites).
        - Remove edges as we process courses, updating in-degrees.
        - If all nodes are processed, return the topological order.
        - If there's a cycle (not all nodes processed), return [].
        """

        # Step 1: Build graph and in-degree map
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1

        # Step 2: Start with courses having no prerequisites
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        topo_order = []

        # Step 3: Process courses
        while queue:
            course = queue.popleft()
            topo_order.append(course)

            for neighbor in graph[course]:
                indegree[neighbor] -= 1  # Remove the edge
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check if all courses are processed
        if len(topo_order) == numCourses:
            return topo_order
        else:
            return []  # Cycle detected, can't finish all courses