class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {} # (str1,str2) -> cost

        if word1 == word2:
            return 0
        
        def cost(str1, str2):
            if len(str1) == 0 or  len(str2) == 0:
                return max(len(str1),len(str2))
            
            if (str1, str2) in memo:
                return memo[(str1,str2)]

            if str1[0] == str2[0]:
                op = 0 + cost(str1[1:],str2[1:])
            else:
                op = 1 + min(cost(str1[1:],str2[1:]),cost(str1,str2[1:]),cost(str1[1:],str2))
            
            memo[(str1,str2)] = op

            return memo[(str1,str2)]

        return cost(word1,word2)