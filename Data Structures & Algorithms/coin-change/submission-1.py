class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        def searchDFS(am):
            if am == 0:
                return 0
            if am in memo:
                return memo[am]
            res = 1e9
            for c in coins:
                if am - c >= 0:
                    res = min(res,1+searchDFS(am-c))
            memo[am] = res
            return res
        minCoins = searchDFS(amount)
        return -1 if minCoins >= 1e9 else minCoins

        