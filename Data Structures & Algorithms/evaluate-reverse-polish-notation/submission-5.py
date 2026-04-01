class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            try:
                if int(i) >= -1000 and int(i) <= 1000:
                    stack.append(i)
            except ValueError:
                a = int(stack[-1])
                stack.pop()
                b = int(stack[-1])
                stack.pop()
                if i == "+":
                    stack.append(int(b + a))
                elif i == "-":
                    stack.append(int(b - a))
                elif i == "*":
                    stack.append(int(b * a))
                elif i == "/":
                    stack.append(int(b / a))
                print(a, b, i)
                print(stack)
        return stack[-1]
