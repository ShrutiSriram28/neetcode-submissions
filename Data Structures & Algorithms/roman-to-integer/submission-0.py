class Solution:
    def romanToInt(self, s: str) -> int:
        stack = []

        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        integer = 0
        for c in s:
            if not stack or roman[c] <= stack[-1]:
                stack.append(roman[c])
            if stack and roman[c] > stack[-1]:
                sub = stack.pop(-1)
                stack.append(roman[c] - sub)
        
        while stack:
            integer += stack.pop(-1)

        return integer