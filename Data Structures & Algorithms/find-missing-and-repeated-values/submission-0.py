class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        seen=set()
        repeat=0
        total=n*n
        
        for row in grid:
            for x in row:
                if x in seen:
                    repeat=x
                seen.add(x)
        
        for x in range(1,total+1):
            if x not in seen:
                return [repeat,x]