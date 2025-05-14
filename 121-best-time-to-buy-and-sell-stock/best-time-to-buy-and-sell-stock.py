class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max profit
        # i = 0, j = loop through array
        # if i > j, update i = j (to sell lower)
        # else, update max profit
        profit = 0
        i = 0
        for j in range(len(prices)):
            if prices[i] >= prices[j]: 
                i = j
            else: 
                profit = max(profit, prices[j] - prices[i])
        return profit
        