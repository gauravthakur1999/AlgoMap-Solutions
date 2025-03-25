class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = float('inf')
        l = 0
        curt = 0
        for r in range(len(nums)):
            curt += nums[r]

            if curt >= target:
                while curt >= target:
                    size = min(size , (r - l + 1))
                    curt -= nums[l]
                    l += 1
        
        return size if size != float('inf') else 0