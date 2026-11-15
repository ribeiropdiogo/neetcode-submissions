class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n, res = len(nums), float('-inf')
        pre = suf = 1
        for i in range(n):
            pre = (pre or 1) * nums[i]
            suf = (suf or 1) * nums[n - 1 - i]
            res = max(res, pre, suf)
        return res
#         0 1  2 3
# nums = [2,4,-3,5]
#         2 8
#                5
# nums = [-3,0,-2]
#         -3 0 -2
# nums = [-3,0,-2,-4]
#         -3 0 -2  8

