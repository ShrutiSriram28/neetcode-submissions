class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # minl = [100] * len(prices)
        # maxr = [0] * len(prices)
        # diff = [0] * len(prices)

        # minl[0] = prices[0]
        # for i in range(1, len(prices)):
        #     minl[i] = min(minl[i-1], prices[i])
        
        # maxr[len(prices) - 1] = prices[len(prices) - 1]
        # for i in range(len(prices) - 2, -1, -1):
        #     maxr[i] = max(maxr[i+1], prices[i])
        
        # for i in range(len(prices)):
        #     diff[i] = maxr[i] - minl[i]

        # profit = max(diff)

        # if profit < 0:
        #     return 0
        
        # return profit

        profit = 0
        
        if len(prices) <= 1:
            return 0

        l = 0
        r = 1

        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
                r += 1
                continue
            profit = max(profit, prices[r] - prices[l])
            r += 1
        
        return profit

        # 5 1 5 6 7 1
        # l r
        #   l r
        #   l   r
        #   l     r
        #   l       r
        #           l 