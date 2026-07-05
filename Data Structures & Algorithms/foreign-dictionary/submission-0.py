class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        chars = set()
        for word in words:
            for ch in word:
                chars.add(ch)
        graph = {ch: set() for ch in chars}
        indegree = {ch: 0 for ch in chars}
        for i in range(len(words) - 1):
            a = words[i]
            b = words[i + 1]
            if len(a) > len(b) and a.startswith(b):
                return ""
            limit = min(len(a), len(b))
            for j in range(limit):
                if a[j] != b[j]:
                    if b[j] not in graph[a[j]]:
                        graph[a[j]].add(b[j])
                        indegree[b[j]] += 1
                    break
        q = deque()
        for ch in chars:
            if indegree[ch] == 0:
                q.append(ch)
        ans = []
        while q:
            ch = q.popleft()
            ans.append(ch)
            for nxt in graph[ch]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        if len(ans) != len(chars):
            return ""
        return "".join(ans)