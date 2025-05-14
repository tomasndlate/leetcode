class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, i = 0, 0
        for j in range(len(prices)):
            # no profit in interval
            if prices[i] >= prices[j]:
                # update to sell lower
                i = j 
            # found a possible profit
            else: 
                profit = max(profit, prices[j] - prices[i])
        return profit
        