class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q, seen = deque(), set()
        res, oranges = 0, 0
        # Start by finding rotten oranges
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r,c,0))
                    seen.add((r,c))
                elif grid[r][c] == 1:
                    oranges += 1
        # Start BFS from rotten oranges
        while q:
            r,c,t = q.popleft()
            if t > res:
                res = t
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1 and (nr,nc) not in seen:
                    q.append((nr,nc,t+1))
                    seen.add((nr,nc))
                    oranges -= 1
        return res if oranges == 0 else -1



#    0          1          2          3          4
# [1,1,0]    [1,1,0]    [1,1,0]    [1,2,0]    [2,2,0]  
# [0,1,1] -> [0,1,2] -> [0,2,2] -> [0,2,2] -> [0,2,2]
# [0,1,2]    [0,2,2]    [0,2,2]    [0,2,2]    [0,2,2]

#     0             1            2               3          4
# [-1,-1,-1]    [-1,-1,-1]    [-1,-1,-1]    [-1, 3,-1]    [ 4, 3,-1]  
# [-1,-1,-1] -> [-1,-1, 1] -> [-1, 2, 1] -> [-1, 2, 1] -> [-1, 2, 1]
# [-1,-1, 0]    [-1, 1, 0]    [-1, 1, 0]    [-1, 1, 0]    [-1, 1, 0]