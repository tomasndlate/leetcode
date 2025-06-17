class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(remaining):
            if remaining in cache:
                return cache[remaining]
            if remaining == 0:
                return 0

            minCoins = amount + 1
            for i in range(len(coins)):
                if remaining - coins[i] >= 0:
                    res = dfs(remaining - coins[i])
                    #if res != -1:
                    minCoins = min(minCoins, 1 + res)
            
            cache[remaining] = minCoins #if minCoins <= amount else -1
            return cache[remaining]
        
        res = dfs(amount)
        return res if res <= amount else -1
            