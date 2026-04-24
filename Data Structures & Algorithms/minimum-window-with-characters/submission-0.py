class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = {}
        have = 0
        need_count = len(need)
        l = 0
        res = ""
        min_len = float('inf')
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in need and window[c] == need[c]:
                have += 1
            while have == need_count:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    res = s[l:r+1]
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1
        return res