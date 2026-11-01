class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        ans = []
        
        if n < 4 or n > 12:
            return ans
            
        def valid(p):
            if len(p) > 1 and p[0] == '0':
                return False
            if int(p) > 255:
                return False
            return True
            
        for i in range(1, n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    p1 = s[:i]
                    p2 = s[i:j]
                    p3 = s[j:k]
                    p4 = s[k:]
                    
                    if valid(p1) and valid(p2) and valid(p3) and valid(p4):
                        ans.append(p1 + "." + p2 + "." + p3 + "." + p4)
                        
        return ans