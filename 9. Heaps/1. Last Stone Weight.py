class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Approach:
        - Simulate the process of repeatedly smashing the two heaviest stones.
        - Use a max-heap to efficiently get the largest two stones.
        - Python only provides a min-heap, so we insert negative values to simulate a max-heap.
        - Repeatedly pop two largest stones:
            - If they're not equal, push the difference back into the heap.
        - When one or zero stones are left, return the last remaining weight (or 0 if none).
        """

        # Convert all stone weights to negatives to simulate a max-heap
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            # Pop two largest stones (remember they are negative)
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            # If they're not equal, push the difference back into the heap
            if first != second:
                heapq.heappush(stones, -(first - second))

        # Return the remaining stone or 0 if none
        return -stones[0] if stones else 0