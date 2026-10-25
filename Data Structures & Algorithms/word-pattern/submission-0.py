class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        a=s.split()
        if len(pattern)!=len(a):
            return False
        mp={}
        used=set()
        for x,y in zip(pattern,a):
            if x in mp:
                if mp[x]!=y:
                    return False
            else:
                if y in used:
                    return False
                mp[x]=y
                used.add(y)
        return True