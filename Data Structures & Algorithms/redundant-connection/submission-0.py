class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n + 1)]
        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]
        for u, v in edges:
            pu = find(u)
            pv = find(v)
            if pu == pv:
                return [u, v]
            par[pu] = pv
        return []