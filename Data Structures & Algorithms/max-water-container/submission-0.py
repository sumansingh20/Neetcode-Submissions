class Solution:
    def maxArea(self, h):
        l,r=0,len(h)-1
        a=0
        while l<r:
            a=max(a,min(h[l],h[r])*(r-l))
            if h[l]<h[r]: l+=1
            else: r-=1
        return a