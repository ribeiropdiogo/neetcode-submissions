class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        def dfs(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(dfs(i+1),nums[i]+dfs(i+2))
            return memo[i]

        return dfs(0)


    # haul [4,4,3,3,0,0]
    # nums [1,1,3,3]
    #       x   x
    #         x   x

    # max(1st,2nd)
    # 2nd + rob(4-end)