class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = r + 1

        while l <= r:
            mid = (l + r)//2

            time = 0
            for p in piles:
                time += math.ceil(p / mid)
            
            if time <= h:
                r = mid - 1
                k = mid
            else:
                l = mid + 1

        return k