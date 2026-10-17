class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, 0 + len(s1)
        aux = sorted(s1)

        if len(s1) > len(s2):
            return False

        while r <= len(s2):
            if sorted(s2[l:r]) == aux:
                return True
            else:
                l, r = l + 1, r + 1
        
        return False
