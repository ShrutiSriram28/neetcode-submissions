class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif t == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif t == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif t == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(t))
        
        output = stack.pop()
        return output









































        # stack = []

        # for c in tokens:
        #     if c == "+":
        #         a = stack.pop()
        #         b = stack.pop()
        #         stack.append(int(b) + int(a))
        #     elif c == "-":
        #         a = stack.pop()
        #         b = stack.pop()
        #         stack.append(int(b) - int(a))
        #     elif c == "*":
        #         a = stack.pop()
        #         b = stack.pop()
        #         stack.append(int(b) * int(a))
        #     elif c == "/":
        #         a = stack.pop()
        #         b = stack.pop()
        #         stack.append(int(b) / int(a))
        #     else:
        #         stack.append(c)
        
        # value = int(stack.pop())
        # return value