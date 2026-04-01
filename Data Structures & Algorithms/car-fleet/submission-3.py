class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse = True)

        for i in range(len(pair)):
            ttr = (target - pair[i][0])/pair[i][1]
            if len(stack) == 0 or ttr > stack[-1]:
                stack.append(ttr)
                
        return len(stack)


# position    target - position   speed   time
# 4           6                   2       3
# 1           9                   2       4.5
# 0           10                  1       10
# 7           3                   1       3