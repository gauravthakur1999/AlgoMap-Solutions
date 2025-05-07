class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Approach:
        - Build the graph and in-degree list.
        - Use Kahn’s algorithm (BFS topological sort) to detect cycles.
        - If we can visit all courses, return True.
        - Otherwise, a cycle exists → return False.
        """

        # Step 1: Build graph and in-degree list
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1

        # Step 2: Queue of nodes with no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        taken_courses = 0

        # Step 3: BFS topological sort
        while queue:
            course = queue.popleft()
            taken_courses += 1

            for neighbor in graph[course]:
                in_degree[neighbor] -= 1  # Remove dependency
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check if all courses were taken
        return taken_courses == numCourses