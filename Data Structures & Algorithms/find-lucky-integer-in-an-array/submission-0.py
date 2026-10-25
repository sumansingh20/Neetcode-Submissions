class Solution:
    def findLucky(self, arr: List[int]) -> int:
        a={}
        
        for x in arr:
            a[x]=a.get(x,0)+1
        
        ans=-1
        
        for x in a:
            if a[x]==x:
                ans=max(ans,x)
        
        return ans