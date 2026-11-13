class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = total // 2
        n = len(nums)
        if n <= 1 or total % 2 != 0:
            return False
        memo = [[-1] * (target+1) for _ in range(n+1)]
        def dfs(i, target):
            if target == 0:
                return True
            if i >= n or target < 0:
                return False
            if memo[i][target] != -1:
                return memo[i][target]
            memo[i][target] = (dfs(i + 1, target) or
                               dfs(i + 1, target - nums[i]))
            return memo[i][target]

        return dfs(0,target)


#         0 1 2 3
# nums = [1,2,3,4]
# 
# T  = 10 / 2 = 5      
#                                  
#                      -[1,2][3,4] x if sum(s2) > T/2 return
#           -[1,2,3][4]-[1,3][2,4] x
#                      -[2,3][1,4] ok
#                      -[1,2][3,4] x
#           -[1,2,4][3]-[1,4][2,3] ok
#                      -[2,4][1,3] - [2][1,3,4] x
#                                  - [4][1,2,3] x
#                      -[1,3][2,4]x
# [1,2,3,4] -[1,3,4][2]-[1,4][2,3]ok
#                      -[3,4][1,2]-[3][1,2,4] x
#                                 -[4][1,2,3] x
#                      -[2,3][1,4] ok
#           -[2,3,4][1]-[2,4][1,3] x
#                      -[3,4][1,2]x
#
#      0  1  2  3  4  5
#   0 -1 -1 -1 -1 -1 -1
#   1 -1 -1 -1 -1 -1 -1
#   2 -1 -1 -1 -1 -1 -1
#   3 -1 -1 -1 -1 -1 -1
#   4 -1 -1 -1 -1 -1 -1
