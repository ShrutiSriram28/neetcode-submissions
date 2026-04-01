import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        min_k = 1

        while l <= r:
            k = (l + r)//2
            time = sum([math.ceil(i / k) for i in piles])
            if time > h:
                l = k + 1
            else:
                min_k = k
                r = k - 1

        return min_k 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # l = 1
        # r = max(piles)
        # k = 1

        # while l <= r:
        #     mid = (l + r)//2
        #     time = sum([math.ceil(p/mid) for p in piles])

        #     if time > h:
        #         l = mid + 1
        #     else:
        #         k = mid
        #         r = mid - 1
        
        # return k