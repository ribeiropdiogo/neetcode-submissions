class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)
        
        need = len(count1)
        for l in range(len(s2)):
            count2, cur = {}, 0
            for r in range(l, len(s2)):
                count2[s2[r]] = 1 + count2.get(s2[r], 0)
                if count1.get(s2[r], 0) < count2.get(s2[r], 0):
                    break
                if count1.get(s2[r], 0) == count2.get(s2[r], 0):
                    cur += 1
                if cur == need:
                    return True
        return False
