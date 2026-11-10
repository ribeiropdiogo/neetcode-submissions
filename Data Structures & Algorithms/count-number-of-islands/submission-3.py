class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def dfs(i,j):
            if i not in range(len(grid)) or j not in range(len(grid[0])):
                return
            if grid[i][j] != "1":
                return
            grid[i][j] = "-1"
            for x,y in directions:
                dfs(i+x,j+y)
            

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i,j)
                print(".")
        
        return res

# grid = [
#    ["-1","1","0","0","1"],
#    ["-1","1","0","0","1"],
#    ["0","0","1","0","0"],
#    ["0","0","0","1","1"]
#  ]              