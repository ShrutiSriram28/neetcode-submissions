class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(diff) < 0:
            return -1
        total = 0
        ind = 0
        for i in range(len(diff)):
            total += diff[i]
            if total < 0:
                ind = i + 1
                total = 0
        return ind
