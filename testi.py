from array import array

class MinHeap:
    
    def __init__(self, initialCapacity=10):
        self.array = Array(initialCapacity)
        self.size = 0
        
    
    def min_heapify(self,i = 0):
        largest = i
        left = (i*2)+1
        right = (i*2)+2
        
        a = self.array
        
        if left < self.size and a[left] < a[largest]:
            largest = left
        if right < self.size and a[right] < a[largest]:
            largest = right

        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            self.min_heapify(largest)
    
    # "kurkistetaan kekoon"
    def peek(self):
        return self.array[0]
    
    def pop(self):
        val = self.array[0]
        if self.size > 1:
            self.array[0] = self.array[self.size-1]
            self.array[self.size-1] = None
        self.size -= 1
        self.min_heapify()
        return val       



    def push(self,value):
        
        if self.size == len(self.array): # onko tilaa?
            self._grow()
        
        self.array[self.size] = value
        self.size += 1
        
        if self.size == 1:
            return # first value added.
        
        current_index = self.size-1
        parent_index = int((current_index-1)/2)
        
        array = self.array
        while current_index != parent_index:

            if array[current_index] < array[parent_index]:
                
                tmp = array[current_index]
                array[current_index] = array[parent_index]
                array[parent_index] = tmp
                
                current_index = parent_index
                parent_index = int((current_index-1)/2)
            else:
                break
        

        
    def _grow(self):
        new_array = Array(len(self.array)*2)
        for i in range(len(self.array)):
            new_array[i] = self.array[i]
        
        self.array = new_array
    
    def __str__(self):
        s = "["
        for i in range(self.size):
            s+=repr(self.array[i])
            if i != self.size-1:
                s+=","
                
        return s+"]"
    
    def __len__(self):
        return self.size
    
    def _print_heap_form(self):
        level = 1
        printed = 0
        for i in range(self.size):
            print(self.array[i],end=" ")
            printed+=1
            if printed ==level:
                level *= 2
                printed = 0
                print()
        print()
    
    
if __name__ == "__main__":
    h = MinHeap()
    
    import random
    
    for i in range(32):
        h.push(random.randint(1,100))
     
     
    l = []
    while len(h)>0:
       x =  h.pop()
       l.append(x)
       
    if l != sorted(l):
        print("EI TOIMINUT")
    print(l)
    
    
