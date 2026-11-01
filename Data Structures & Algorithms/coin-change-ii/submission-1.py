class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1

        for c in range(len(coins)-1,-1,-1):
            dpNext = [0] * (amount+1)
            dpNext[0] = 1
            for a in range(1,amount+1):
                dpNext[a] = dp[a]
                if a - coins[c] >= 0:
                    dpNext[a] += dpNext[a - coins[c]]
            dp = dpNext
        return dp[amount]