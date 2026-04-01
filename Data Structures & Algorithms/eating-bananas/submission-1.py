class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles.sort()

        l = 1
        r = max(piles)
        k = l

        while l <= r:
            mid = (l + r) // 2
            total_time = 0
            for i in range(len(piles)):
                total_time += math.ceil(piles[i]/mid)
            if total_time <= h:
                k = mid
                r = mid - 1
            else:
                l = mid + 1
        return k