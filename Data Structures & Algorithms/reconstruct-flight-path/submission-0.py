class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        tickets.sort(reverse=True)
        for a, b in tickets:
            if a not in graph:
                graph[a] = []
            graph[a].append(b)
        ans = []
        def dfs(node):
            while node in graph and graph[node]:
                dfs(graph[node].pop())
            ans.append(node)
        dfs("JFK")
        return ans[::-1]