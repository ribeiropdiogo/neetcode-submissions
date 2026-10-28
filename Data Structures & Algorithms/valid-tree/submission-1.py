class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Check if tree has n  1 edges
        if len(edges) > (n-1):
            return False
        # Build adjancey map
        adjMap = {v: [] for v in range(n)}
        # Populate adjancency map
        for o,d in edges:
            adjMap[o].append(d)
            adjMap[d].append(o)

        visited = set()
        def dfs(parent,v):
            if v in visited:
                return False
            visited.add(v)
            for nv in adjMap[v]:
                if nv is not parent:
                    if dfs(v,nv) == False:
                        return False
            return True
                 
        return dfs(-1,0) and len(visited) == n
