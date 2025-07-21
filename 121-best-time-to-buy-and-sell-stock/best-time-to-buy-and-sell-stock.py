class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowestStock = prices[0]

        for price in prices[1:]:
            lowestStock = min(lowestStock, price)
            profit = max(profit, price - lowestStock)
        
        return profit