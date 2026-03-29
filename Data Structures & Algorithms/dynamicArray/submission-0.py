class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [null] * capacity
        self.capacity = capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        # if full, resize
        if self.getSize() >= self.getCapacity():
            resize()

        self.array[size] = n
        self.size += 1

    def popback(self) -> int:
        popped_item = self.array[self.size]
        self.array[self.size] = null

        self.size -= 1
        return popped_item


    def resize(self) -> None:
        temp_array = [] * (capacity * 2) 

        for i in range(size):
            temp_array[i] = self.array[i]

        self.array = temp_array

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity