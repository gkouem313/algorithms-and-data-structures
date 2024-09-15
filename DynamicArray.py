class DynamicArray:

    def __init__(self, capacity: int):
        self.array = [0] * capacity
        self.capacity = capacity
        self.size = 0


    def get(self, i: int) -> int:
        return self.array[i]
    
    
    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:
        if (self.size == self.capacity):
            self.resize()
        self.array[self.size] = n
        self.size += 1


    def popback(self) -> int:
        self.size -= 1
        return self.array[self.size]
    

    def resize(self) -> None:
        self.capacity *= 2
        new_array = [0] * self.capacity
        for i in range(0, self.size):
            new_array[i] = self.array[i]
        self.array = new_array


    def getCapacity(self) -> int:
        return self.capacity
    
    
    def getSize(self) -> int:
        return self.size