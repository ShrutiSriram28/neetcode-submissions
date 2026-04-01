class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for o in operations:
            if o == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(b)
                stack.append(a)
                stack.append(str(int(a) + int(b)))
            elif o == "D":
                a = stack.pop()
                stack.append(a)
                stack.append(str(int(a) * 2))
            elif o == "C":
                stack.pop()
            else:
                stack.append(o)
        
        score = 0
        while stack:
            score += int(stack.pop())

        return score