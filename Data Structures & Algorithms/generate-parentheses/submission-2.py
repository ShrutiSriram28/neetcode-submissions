class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        output = []

        def gen(o, c):
            if o == c == n:
                output.append("".join(stack))
                return
            if o < n:
                stack.append("(")
                gen(o + 1, c)
                stack.pop()
            if c < o:
                stack.append(")")
                gen(o, c + 1)
                stack.pop()
        
        gen(0, 0)
        return output
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # stack = []
        # output = []
        # def appendParanthesis(openn, closen):
        #     if openn == closen == n:
        #         output.append("".join(stack))
        #         return
            
        #     if openn < n:
        #         stack.append("(")
        #         appendParanthesis(openn + 1, closen)
        #         stack.pop()
        #     if closen < openn:
        #         stack.append(")")
        #         appendParanthesis(openn, closen + 1)
        #         stack.pop()

        # appendParanthesis(0, 0)
        
        # return output