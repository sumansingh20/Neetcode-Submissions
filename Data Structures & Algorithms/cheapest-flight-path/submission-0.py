class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        d = [float('inf')] * n
        d[src] = 0
        
        for _ in range(k + 1):
            t = list(d)
            for u, v, w in flights:
                if d[u] != float('inf') and d[u] + w < t[v]:
                    t[v] = d[u] + w
            d = t
            
        if d[dst] == float('inf'):
            return -1
        return d[dst]