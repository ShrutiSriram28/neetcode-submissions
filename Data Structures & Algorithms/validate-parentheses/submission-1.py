class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        braces = {'(':')', '[':']', '{':'}'}
        for c in s:
            if c in braces:
                stack.append(c)
            elif (len(stack) == 0 or braces[stack[-1]] != c) and (c == ')' or c == ']' or c == '}'):
                return False
            elif braces[stack[-1]] == c:
                stack.pop()
        
        return not stack