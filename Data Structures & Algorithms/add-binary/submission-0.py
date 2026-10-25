class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        ans = []
        
        while i >= 0 or j >= 0 or carry > 0:
            total = carry
            
            if i >= 0:
                total = total + int(a[i])
                i = i - 1
                
            if j >= 0:
                total = total + int(b[j])
                j = j - 1
                
            ans.append(str(total % 2))
            carry = total // 2
            
        ans.reverse()
        return "".join(ans)