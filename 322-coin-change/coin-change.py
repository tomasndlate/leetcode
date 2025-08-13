class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dp(remaining):
            if remaining in cache:
                return cache[remaining]
            if remaining == 0:
                return 0
            if remaining < 0:
                return -1

            min_coins = float('inf')
            for coin in coins:
                used = dp(remaining - coin)
                if used > -1:
                    min_coins = min(min_coins, used + 1)
            
            cache[remaining] = min_coins if min_coins != float('inf') else -1
            return cache[remaining]

        return dp(amount)