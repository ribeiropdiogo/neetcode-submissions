class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 
        # Get rotation point O(logn)
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m + 1  # drop somewhere right of m, and m itself can't be the minimum
            else:
                r = m      # m..r is sorted, so the minimum is m or to its left
        pivot = l
        # Pick the sorted half that could contain target
        if nums[pivot] <= target <= nums[-1]:
            l, r = pivot, len(nums)-1
        else:
            l, r = 0, pivot-1
        # Binary search
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m-1
            else:
                l = m+1
        return -1
#         0 1 2 3 4 5
# nums = [1,2,3,4,5,6]
# nums = [3,4,5,6,1,2] n = 4
# t = 1   l       p r
#               