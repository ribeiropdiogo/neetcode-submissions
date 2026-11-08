class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0 for i in range(len(text2)+1)]
        
        for i in range(len(text1)-1,-1,-1):
            newDP = [0 for i in range(len(text2)+1)]
            for j in range(len(text2)-1,-1,-1):
                if text1[i] == text2[j]:
                    newDP[j] = 1 + dp[j+1]
                else:
                    newDP[j] = max(dp[j],newDP[j+1])
            dp = newDP

        return dp[0]

#  c r a b t 
#c 3 2 2 1 1 0 | 
#a 2 2 2 1 1 0 | 
#t 1 1 1 1 1 0 | 1
#  0 0 0 0 0 0

