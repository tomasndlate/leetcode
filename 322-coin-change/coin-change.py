class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        cache = {}

        def dp(remaining):
            if remaining == 0:
                return 0 # found solution
            if remaining < 0:
                return -1 # impossible
            if remaining in cache:
                return cache[remaining]
            
            minCoins = float('inf')
            
            for coin in coins:
                usedCoins = dp(remaining - coin)
                if usedCoins >= 0:
                    minCoins = min(minCoins, 1 + usedCoins)
            
            cache[remaining] = minCoins if minCoins != float('inf') else -1
            return cache[remaining]
        
        return dp(amount)