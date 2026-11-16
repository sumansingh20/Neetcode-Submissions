class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        return __import__('functools').reduce(lambda a, b: (a[0]+1, a[1], a[2]) if b==5 else (a[0]-1, a[1]+1, a[2] and a[0]>0) if b==10 else (a[0]-1, a[1]-1, a[2]) if a[1]>0 and a[0]>0 else (a[0]-3, a[1], a[2]) if a[0]>=3 else (a[0], a[1], False), bills, (0, 0, True))[2]
