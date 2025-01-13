class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for n in nums:
            if abs(n) < abs(res):
                res = n
        if res < 0 and abs(res) in nums:
            return abs(res)
        else:
            return res