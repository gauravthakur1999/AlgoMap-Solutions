class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Approach:
        - Use a max-heap to keep track of the k closest points to the origin.
        - Push (-distance, point) to simulate max-heap behavior with heapq (which is min-heap by default).
        - If heap size exceeds k, pop the farthest point.
        - Finally, extract the point coordinates from the heap using a for-loop.
        """

        max_heap = []  # (-distance, point)
        res = []

        for x, y in points:
            dist = x ** 2 + y ** 2  # Squared distance from origin
            heapq.heappush(max_heap, (-dist, [x, y]))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        # Extract the k closest points from the heap
        for _, point in max_heap:
            res.append(point)

        return res