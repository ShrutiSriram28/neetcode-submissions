class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            a, b = 0, 0
            if i == "+":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b + a)
            elif i == "-":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b - a)
            elif i == "*":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b * a)
            elif i == "/":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(int(b / a))
            else:
                stack.append(i)
        return stack[-1]
