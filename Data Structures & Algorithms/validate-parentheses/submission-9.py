class Solution:
    def isValid(self, s: str) -> bool:
        pair = {')':'(', ']':'[', '}':'{'}
        stack = []

        for c in s:
            if c in pair.values():
                stack.append(c)
            elif not stack and c in pair.keys():
                return False
            elif stack and pair[c] == stack[-1]:
                stack.pop()
            else:
                return False

        return True if len(stack) == 0 else False