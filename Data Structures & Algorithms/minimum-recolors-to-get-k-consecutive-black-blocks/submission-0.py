class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans=k
        w=0
        
        for i in range(len(blocks)):
            if blocks[i]=='W':
                w+=1
            
            if i>=k and blocks[i-k]=='W':
                w-=1
            
            if i>=k-1:
                ans=min(ans,w)
        
        return ans