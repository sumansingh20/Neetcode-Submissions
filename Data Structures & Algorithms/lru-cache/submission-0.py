class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.suman = {}
    def get(self, key: int) -> int:
        if key not in self.suman:
            return -1
        temp = self.suman[key]
        del self.suman[key]
        self.suman[key] = temp
        return temp
    def put(self, key: int, value: int) -> None:
        if key in self.suman:
            del self.suman[key]
        elif len(self.suman) == self.capacity:
            temp = next(iter(self.suman))
            del self.suman[temp]
        self.suman[key] = value