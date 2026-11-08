class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i,val):
            if i == len(nums):
                return 1 if val == target else 0
            if (i,val) in memo:
                return memo[(i,val)]
            memo[(i,val)] = dfs(i+1,val+nums[i]) + dfs(i+1,val-nums[i])
            return memo[(i,val)]
        return dfs(0,0)

# 0   1   2
#            - 6
#       - 4 
#            - 2 (x)
#   - 2      - 2 (x)
#       - 0
#            - -2
# 0
#            - 2 (x)
#       - 0
#            - -2
#   - -2
#            - -2
#       - -4
#            - -6
#
#
