class Solution:
    def getWater(self, h1: int, h2: int, d: int) -> int:
        return min(h1,h2)*d

    def maxArea(self, heights: List[int]) -> int:
        maxw = 0
        l, r = 0, len(heights) -1
        while l < r:
            area = self.getWater(heights[l],heights[r],r-l)
            if area > maxw:
                maxw = area
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return maxw