class Solution:
    def rob(self, nums: List[int]) -> int:
        # Iterate the houses backwards
        for i in range(len(nums)-1,-1,-1):
            if i < len(nums)-2:
                maxRob = 0
                # Iterate all possible next houses
                for j in range(i+2,len(nums)):
                    maxRob = max(maxRob,nums[j])
                nums[i] = nums[i] + maxRob
        # Return the highest of the two counters
        return max(nums[0],nums[1]) if len(nums) > 1 else nums[0]
