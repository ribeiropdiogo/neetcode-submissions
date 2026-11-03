class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n-1

        for i in range(n-1,-1,-1):
            for j in range(0,nums[i]+1):
                if i+j == goal:
                    goal = i

        return True if goal == 0 else False
        
        
