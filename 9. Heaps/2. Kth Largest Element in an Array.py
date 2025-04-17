class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Approach:
        - Use Python's heapq to create a min-heap from the input list.
        - Since heapq is a min-heap, the smallest element is at the root.
        - We want the k-th largest element, so we remove the smallest (n - k) elements.
        - The next pop will give us the k-th largest element.
        """

        heapq.heapify(nums)  # Step 1: Convert list into a min-heap

        # Step 2: Remove the smallest (n - k) elements from the heap
        while len(nums) > k:
            heapq.heappop(nums)

        # Step 3: The root of the heap is now the k-th largest element
        return heapq.heappop(nums)