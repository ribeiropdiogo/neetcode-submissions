class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r, goal = 0, 0, len(nums)-1
        while l < goal and r < goal:
            r += max(nums[l:r+1])
            l += 1
        return l