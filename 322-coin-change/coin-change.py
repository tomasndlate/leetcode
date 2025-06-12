class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(total):
            if total == 0:
                return 0
            if total in cache:
                return cache[total]
            
            res = float('inf')
            for coin in coins:
                if total - coin >= 0:
                    res = min(res, 1 + dfs(total - coin))
            
            cache[total] = res
            return res

        minCoins = dfs(amount)
        return minCoins if minCoins != float('inf') else -1