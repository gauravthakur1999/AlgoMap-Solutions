class Solution:
    def fib(self, n: int) -> int:
        first = 0
        second = 1
        if n == 0:
            return first
        elif n == 1:
            return second
        else:
            while n > 1:
                temp = first + second
                first = second
                second = temp
                n -= 1
        return second