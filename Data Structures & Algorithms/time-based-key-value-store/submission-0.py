class TimeMap:
    def __init__(self):
        self.suman = {}
    def set(self, key, value, timestamp):
        if key not in self.suman:
            self.suman[key] = []
        self.suman[key].append((timestamp, value))
    def get(self, key, timestamp):
        if key not in self.suman:
            return ""
        arr = self.suman[key]
        l, r = 0, len(arr)-1
        ans = ""
        
        while l <= r:
            mid = (l+r)//2
            
            if arr[mid][0] <= timestamp:
                ans = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return ans