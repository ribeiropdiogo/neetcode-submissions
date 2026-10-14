class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False

        freq = [0]*26

        for i in s:
            freq[ord(i)-ord('a')] += 1
        for j in t:
            freq[ord(j)-ord('a')] -= 1

        for count in freq:
            if count != 0:
                return False
        return True

        