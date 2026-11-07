class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        i, j = 0, 0
        substr = []

        if len(s) == 0:
            return 0

        while j < len(s):
            if s[j] in substr:
                ind = (substr.index(s[j])+1)
                substr = substr[ind:]
                i += (ind+1)
            substr.append(s[j])
            res = max(res,len(substr))
            j += 1
        return res


        # s = "pwwkew" -> 
        #      i
        #        j
        # res = 2
        # substr = pw