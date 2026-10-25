class MyHashSet:
    def __init__(self):
        self.a=[False]*1000001

    def add(self, key: int) -> None:
        self.a[key]=True

    def remove(self, key: int) -> None:
        self.a[key]=False

    def contains(self, key: int) -> bool:
        return self.a[key]