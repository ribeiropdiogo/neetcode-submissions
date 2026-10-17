class Solution:
    def search(self, nums: List[int], target: int) -> int:
        partition = len(nums) // 2

        if nums[partition] == target:
            return partition
        
        if len(nums) > 1:
            if nums[partition] < target:
                sub = self.search(nums[partition:], target)
                if sub > -1:
                    return partition + sub
                return sub
            else:
                print(nums[partition:])
                return self.search(nums[0:partition], target)
        else:
            return -1