import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = 1

        while l <= r:
            mid = (l + r)//2
            time = sum([math.ceil(p/mid) for p in piles])

            if time > h:
                l = mid + 1
            else:
                k = mid
                r = mid - 1
        
        return k