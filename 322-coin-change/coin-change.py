class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        memo = {}

        def dp(remaining):
            if remaining in memo: return memo[remaining]
            if remaining < 0: return -1
            if remaining == 0: return 0
            
            usedCoins = amount + 1
            for coin in coins:
                otherCoins = dp(remaining - coin)
                if otherCoins == -1: # impossible to reach
                    continue
                usedCoins = min(usedCoins, 1 + otherCoins)

            memo[remaining] = usedCoins if usedCoins <= amount else -1
            return memo[remaining]
        
        return dp(amount)
                