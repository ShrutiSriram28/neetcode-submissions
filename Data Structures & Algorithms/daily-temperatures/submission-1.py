class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        warmer = [0] * len(temperatures)

        for t in range(len(temperatures)):
            if len(stack) == 0:
                stack.append([t, temperatures[t]])
            elif temperatures[t] <= stack[-1][1]:
                stack.append([t, temperatures[t]]) 
            while len(stack) != 0 and temperatures[t] > stack[-1][1]:
                popped = stack.pop()
                warmer[popped[0]] = t - popped[0]
            stack.append([t, temperatures[t]])
        
        return warmer
