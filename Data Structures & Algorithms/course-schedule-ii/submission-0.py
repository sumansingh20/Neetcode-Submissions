class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        ans = []

        while q:

            node = q.popleft()
            ans.append(node)

            for next_node in graph[node]:

                indegree[next_node] -= 1

                if indegree[next_node] == 0:
                    q.append(next_node)

        if len(ans) == numCourses:
            return ans

        return []