class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Invalid capacity")
        self.array = [None] * capacity
        self.capacity = capacity
        self.size = 0 #number of element currently stored

    def get(self, i: int) -> int:
        #to return the element at index i
        if i >= 0 and i < self.size:
            return self.array[i]
        raise IndexError("Index out of bounds")

    def set(self, i: int, n: int) -> None:
        if 0 <= i < self.size:
            self.array[i] = n
        else:
            raise IndexError("Index out of bounds")

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            # raise Exception("Array is full")
            self.resize()
        self.array[self.size] = n
        self.size += 1


    def popback(self) -> int:
        #to remove the last element in the array
        if self.size == 0:
            raise Exception("Array is Empty")
        val = self.array[self.size - 1]
        self.array[self.size - 1] = None
        self.size -= 1
        return val
        
 

    def resize(self) -> None:
        #to double the capacity of the array
        new_capacity = self.capacity * 2
        new_array= [None] * new_capacity

        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
