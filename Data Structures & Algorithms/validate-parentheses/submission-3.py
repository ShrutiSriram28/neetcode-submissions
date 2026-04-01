class Solution:
    def isValid(self, s: str) -> bool:
        braces = {'(':')', '[':']', '{':'}'}
        stack = []

        for c in s:
            if c in braces.keys():
                stack.append(c)

            elif len(stack) == 0 and c in braces.values():
                return False

            elif c == braces[stack[-1]]:
                stack.pop()

            elif c != braces[stack[-1]]:
                return False

        if len(stack) != 0:
            return False

        return True

