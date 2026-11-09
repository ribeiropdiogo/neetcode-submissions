class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i,a):
            if i == len(coins) or a < 0:
                return 0
            if a == 0:
                return 1
            if (i,a) in memo:
                return memo[(i,a)]
            memo[(i,a)] = dfs(i,a-coins[i]) + dfs(i+1,a)
            return memo[(i,a)]
            
        return dfs(0,amount)

# [1,2,3]
# amount = 4    
#                        - 0,0 ok
#                  - 0,1      - 1,-1 not ok
#                        - 1,1     - 3,-2 not ok
#                             - 2,1
#                                  - 3,1 not ok
#            - 0,2      - 1,0 ok
#                  - 1,2     - 2,-1 not ok
#      - 0,3            - 2,2
#                            - 3,2 not ok
#                 - 1,0 ok
#            - 1,2     - 2,-1 not ok
#                 - 2,2         
# 0,4 
#      - 1,4
#
#


