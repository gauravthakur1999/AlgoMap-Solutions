class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [None for i in range(len(nums))]
        leftprod = 1
        for i in range(len(nums)):
            ans[i] = leftprod
            leftprod = leftprod * nums[i]
        rightprod = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] = ans[i] * rightprod
            rightprod = rightprod * nums[i]
        return ans

        