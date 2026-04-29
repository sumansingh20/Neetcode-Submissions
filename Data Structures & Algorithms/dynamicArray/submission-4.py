class DynamicArray:
    
    def __init__(self, capacity: int):
        self.suman = [0] * capacity
        self.size = 0
        self.cap = capacity

    def get(self, i: int) -> int:
        return self.suman[i]

    def set(self, i: int, n: int) -> None:
        self.suman[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.cap:
            self.resize()
        self.suman[self.size] = n
        self.size += 1

    def popback(self) -> int:
        val = self.suman[self.size - 1]
        self.size -= 1
        return val

    def resize(self) -> None:
        new_cap = self.cap * 2
        temp = [0] * new_cap
        
        for i in range(self.size):
            temp[i] = self.suman[i]
        
        self.suman = temp
        self.cap = new_cap

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.cap