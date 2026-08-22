class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [0] * self.capacity
        self.maxIndex = 0


    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:
        if self.maxIndex == len(self.array):
            self.resize()
        self.array[self.maxIndex] = n
        self.maxIndex += 1
        


    def popback(self) -> int:
        
        val = self.array[self.maxIndex - 1]
        self.maxIndex -= 1
        return val
 

    def resize(self) -> None:
        self.array.extend([0] * len(self.array))



    def getSize(self) -> int:
        return self.maxIndex
        
    
    def getCapacity(self) -> int:
        return len(self.array)
