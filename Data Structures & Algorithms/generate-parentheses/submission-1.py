class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        output = []
        def appendParanthesis(openn, closen):
            if openn == closen == n:
                output.append("".join(stack))
                return
            
            if openn < n:
                stack.append("(")
                appendParanthesis(openn + 1, closen)
                stack.pop()
            if closen < openn:
                stack.append(")")
                appendParanthesis(openn, closen + 1)
                stack.pop()

        appendParanthesis(0, 0)
        
        return output