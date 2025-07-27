class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(remaining):
            if remaining in memo:
                return memo[remaining]
            if remaining == 0:
                return 0
            if remaining < 0:
                return -1

            usedCoins = float('inf')
            for coin in coins:
                otherCoins = dp(remaining - coin)
                if otherCoins == -1:
                    continue
                usedCoins = min(usedCoins, 1 + otherCoins)
            
            memo[remaining] = usedCoins if usedCoins != float('inf') else -1
            return memo[remaining]
        
        return dp(amount)
                