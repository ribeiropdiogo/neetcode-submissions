class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Build adjacency map and populate
        adjMap = {v+1:[] for v in range(len(edges))}
        for ov, dv in edges:
            adjMap[ov].append(dv)
            adjMap[dv].append(ov)

        visited = set()
        def dfs(parent,v):
            if v in visited:
                return
            visited.add(v)
            for nv in adjMap[v]:
                dfs(v,nv)
            return


        # Iterate edge list backwards
        for ov, dv in edges[::-1]:
            # Remove edge
            adjMap[ov].remove(dv)
            adjMap[dv].remove(ov)
            # Test and return edge if graph is valid
            dfs(-1,1)
            if len(visited) == len(edges):
                return [ov,dv]
            visited = set()
            # Add edge again
            adjMap[ov].append(dv)
            adjMap[dv].append(ov)