class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r,c):
            res = 0
            # Return if out of bounds
            if (r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c]==0):
                return 0
            # Mark cell as visited
            grid[r][c] = 0
            # Try all possible directions
            for dr, dc in directions:
                res += dfs(r + dr, c + dc)
            return 1+res

        # Iterate matrix
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res,dfs(r, c))
        return res