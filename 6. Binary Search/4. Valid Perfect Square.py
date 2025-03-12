class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        
        while l <= r:
            m = (l + r) // 2
            m2 = m*m
            if num == m2:
                return True
            elif m2 < num:
                l = m + 1
            else:
                r = m - 1
        
        return False

