class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for opr in operations:
            if opr == '+':
                stack.append(stack[-1] + stack[-2])
            elif opr == 'D':
                stack.append(2 * stack[-1])
            elif opr =='C':
                stack.pop()
            else:
                stack.append(int(opr))
        return sum(stack)