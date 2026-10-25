class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            # Combination is found
            if total == target:
                res.append(cur.copy())
                return
            # Pointer out of bounds or sum over target
            if i >= len(nums) or total > target:
                return
        
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i+1,cur, total)
        
        dfs(0,[],0)
        return res
            