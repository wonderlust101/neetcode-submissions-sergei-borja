class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.capacity <= self.size:
            self.resize()

        self.size += 1
        self.array[self.size] = n

    def popback(self) -> int:
        if self.size <= 0:
            return None
        
        popped_value = self.array[self.size]
        self.array[self.size] = None
        
        self.size -= 1
        return popped_value

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        temp_array = [None] * self.capacity

        for i in range(self.size):
            temp_array[i] = self.array[i]

        self.array = temp_array

    def getSize(self) -> int:
        return self.size
        
    def getCapacity(self) -> int:
        return self.capacity