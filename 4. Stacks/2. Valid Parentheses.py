class Solution:
    def isValid(self, s: str) -> bool:
        close_for = {')':'(', '}': '{', ']':'['}
        stack = []

        for c in s:
            if c in close_for:
                if stack and stack[-1] == close_for[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False