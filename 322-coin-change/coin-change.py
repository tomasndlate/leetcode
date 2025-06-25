class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        coins.sort()

        def dp(remaining):
            if remaining in memo:
                return memo[remaining]
            if remaining == 0:
                return 0
            if remaining < 0:
                return -1

            min_coins = float('inf')
            for coin in reversed(coins):
                res = dp(remaining - coin)
                if res >= 0:
                    min_coins = min(min_coins, 1 + res)
                    
            memo[remaining] = min_coins if min_coins < float('inf') else -1
            return memo[remaining]

        return dp(amount)