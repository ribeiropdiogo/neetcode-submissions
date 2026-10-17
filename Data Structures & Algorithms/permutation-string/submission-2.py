class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, 0 + len(s1)

        while r <= len(s2):
            if sorted(s2[l:r]) == sorted(s1):
                return True
            else:
                l, r = l + 1, r + 1
        
        return False
