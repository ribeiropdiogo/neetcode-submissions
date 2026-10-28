class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        # Build adjacency map
        adjMap = {v:[] for v in range(n)}
        # Populate adjacency map
        for ov,dv in edges:
            adjMap[ov].append(dv)
            adjMap[dv].append(ov)
        
        visited = set()
        def dfs(par,v):
            if v in visited:
                return
            visited.add(v)
            for nv in adjMap[v]:
                dfs(v,nv)
            return

        for v in range(n):
            if v not in visited:
                dfs(-1,v)
                res += 1
        
        return res