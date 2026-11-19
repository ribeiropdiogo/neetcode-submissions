class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        inc, st = [(-1,-1)] * len(temperatures), []
        # Build inc array and aux stack
        for i, x in enumerate(temperatures):
            while st and temperatures[st[-1]] < x:
                curPos = st.pop()
                inc[curPos] = (x, i-curPos)
            st.append(i)
        # Update inc inplace
        for i, pair in enumerate(inc):
            t, pos = pair
            if t == -1:
                inc[i] = 0
            else:
                inc[i] = pos
        return inc
 
#                  0  1  2  3  4  5  6
# temperatures = [30,38,30,36,35,40,28]
#               x        
#   stack   = [-1 -1 -1 -1 -1 -1 -1] 0
#   indices = [0]  x                  
#   stack   = [38 -1 -1 -1 -1 -1 -1] 1
#   indices = [1]     x               
#   stack   = [38 -1 -1 -1 -1 -1 -1] 2 
#   indices = [1,2]      x              
#   stack   = [38 -1 36 -1 -1 -1 -1] 3
#   indices = [1,3]         x              
#   stack   = [38 -1 36 -1 -1 -1 -1] 4
#   indices = [1,3,4]          x              
#   stack   = [38 40 36 40 40 -1 -1] 5
#   indices = [4]                 x              
#   stack   = [38 40 36 40 40 -1 -1] 6
#   indices = [4,1] 
#
# result = [1,4,1,2,1,0,0]   naive: O(n^2) time 
#                                   O(1) space without result
#
#
#
#