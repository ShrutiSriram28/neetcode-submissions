class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse = True)

        stack = []
        stack.append(pair[0])
        
        for i in range(1, len(pair)):

            if (target - pair[i][0])/pair[i][1] > (target - stack[-1][0])/stack[-1][1]:
                stack.append(pair[i])
        
        return len(stack)