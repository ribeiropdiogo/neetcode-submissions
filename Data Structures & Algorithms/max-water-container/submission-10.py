class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAmount, i, j = 0, 0, len(heights)-1
        while i < j:
            amount = min(heights[i],heights[j]) * (j-i)
            maxAmount = max(maxAmount,amount)
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return maxAmount
        # heights = [2,7,2,5,4,7,3,6]
        #              i j
        # 
        # amount = 14 -> 36 -> 15 -> 28 -> 12 -> 10 -> 2
        # 