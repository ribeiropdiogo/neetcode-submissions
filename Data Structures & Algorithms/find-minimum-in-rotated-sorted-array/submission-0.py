class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float('inf')

        while l <= r:
            print(l,r)
            i = l + ((r-l)//2)
            print(i)
            res = min(res, nums[i])
            if nums[i] < nums[r]:
                r = i-1
            else:
                l = i+1

        return res

        