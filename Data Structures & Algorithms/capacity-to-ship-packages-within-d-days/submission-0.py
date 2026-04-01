class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        k = r + 1

        while l <= r:
            mid = (l + r)//2

            total_weight = 0
            total_days = 1
            for w in weights:
                if total_weight + w <= mid:
                    total_weight += w
                else:
                    total_days += 1
                    total_weight = w
                    
            if total_days <= days:
                k = mid
                r = mid - 1
            else:
                l = mid + 1

        return k