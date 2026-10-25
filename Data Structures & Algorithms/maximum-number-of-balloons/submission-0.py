class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b=a=l=o=n=0
        
        for x in text:
            if x=='b':
                b+=1
            elif x=='a':
                a+=1
            elif x=='l':
                l+=1
            elif x=='o':
                o+=1
            elif x=='n':
                n+=1
        
        return min(b,a,l//2,o//2,n)