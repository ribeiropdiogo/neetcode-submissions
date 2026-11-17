class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v,t))
        dist = [float('inf')] * (n+1)
        dist[k] = 0
        h = [(0,k)]
        seen = set()
        while h:
            d, u = heapq.heappop(h)
            seen.add(u)
            if d > dist[u]: continue # there is a shortest path
            for v,t in adj[u]:
                nd = d + t
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(h,(nd,v))
        return -1 if len(seen) < n else max(dist[1:])       