class DynamicArray:
    def __init__(self, capacity):
        self.arr = [0] * capacity
        self.size = 0
        self.capacity = capacity
    def get(self, i):
        return self.arr[i]
    def set(self, i, n):
        self.arr[i] = n
    def pushback(self, n):
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1
    def popback(self):
        self.size -= 1
        return self.arr[self.size]
    def resize(self):
        new_arr = [0] * (self.capacity * 2)
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity *= 2
    def getSize(self):
        return self.size
    def getCapacity(self):
        return self.capacity