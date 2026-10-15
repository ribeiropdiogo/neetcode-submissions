class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        lowers = s.lower()
        while i < j:
            while i < j and not self.alphaNum(lowers[i]):
                i += 1
            while j > i and not self.alphaNum(lowers[j]):
                j -= 1
            if lowers[i] != lowers[j]:
                return False
            i += 1
            j -= 1
        return True
    
    def alphaNum(self, c):
        return (ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
            

        