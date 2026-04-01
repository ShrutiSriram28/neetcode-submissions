import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_ = [-1 * i for i in stones]
        heapq.heapify(stones_)
        while len(stones_) > 1:
            stone1 = -1 * heapq.heappop(stones_)
            stone2 = -1 * heapq.heappop(stones_)
            if abs(stone1 - stone2) > 0:
                heapq.heappush(stones_, -1 * abs(stone1 - stone2))

        if len(stones_) == 0:
            return 0
        else:
            return -1 * stones_[0]
