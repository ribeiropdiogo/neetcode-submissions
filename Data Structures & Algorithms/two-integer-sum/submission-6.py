class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = []
        for i, num in enumerate(nums):
            sorted_nums.append((num,i))
        sorted_nums.sort()
        
        i, j = 0, len(nums) - 1
        while i < j:
            cur = sorted_nums[i][0] + sorted_nums[j][0]
            print(cur)
            if cur == target:
                return[min(sorted_nums[i][1],sorted_nums[j][1]),max(sorted_nums[i][1],sorted_nums[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return []

        