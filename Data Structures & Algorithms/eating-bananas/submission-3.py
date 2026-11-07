class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo+hi)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/mid)
            if hours <= h:
                hi = mid
            else:
                lo = mid + 1
        return hi
# piles [1 4 3 2] 
# hours 2
# lo 1 -> 2 | hi 4 -> 2
# h = 9