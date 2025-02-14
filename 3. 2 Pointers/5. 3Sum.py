class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1,  len(nums) - 1
            while l < r:
                curr_sum  = nums[i] + nums[l] + nums [r]
                if curr_sum > 0:
                    r -= 1
                elif curr_sum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums [r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1 
        return res