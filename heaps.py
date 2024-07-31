import sys

class MinHeap:
    def __init__(self, maxsize):
        # Initialize the heap with a maximum size, size, and a list to hold the heap elements
        self.maxsize = maxsize  
        self.size = 0  
        # Heap list initialized with zero and the first element as a very small value
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize 
        self.FRONT = 1  

    def parent(self, pos):
        # Return the index of the parent of the node at index `pos`
        return pos // 2

    def leftChild(self, pos):
        # Return the index of the left child of the node at index `pos`
        return 2 * pos

    def rightChild(self, pos):
        # Return the index of the right child of the node at index `pos`
        return (2 * pos) + 1

    def isLeaf(self, pos):
        # Check if the node at index `pos` is a leaf node
        return pos * 2 > self.size

    def swap(self, fpos, spos):
        # Swap the elements at indices `fpos` and `spos`
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def minHeapify(self, pos):
        # Ensure the subtree rooted at `pos` obeys the min-heap property
        if not self.isLeaf(pos): 
            # Check if the node at `pos` is greater than either of its children
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or
               self.Heap[pos] > self.Heap[self.rightChild(pos)]):
               
                # If left child is smaller than right child
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos)) 
                    self.minHeapify(self.leftChild(pos))  
                
                else:
                    self.swap(pos, self.rightChild(pos)) 
                    self.minHeapify(self.rightChild(pos))  

    def insert(self, element):
        # Insert a new element into the heap
        if self.size >= self.maxsize:  
            return 
        self.size += 1 
        self.Heap[self.size] = element  
        current = self.size 
        # Bubble up the new element to restore the min-heap property
        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current)) 
            current = self.parent(current) 

    def Print(self):
        # Print the heap structure
        for i in range(1, (self.size // 2) + 1):
            
            print(" PARENT : " + str(self.Heap[i]) + " LEFT CHILD : " +
                  str(self.Heap[2 * i]) + " RIGHT CHILD : " +
                  str(self.Heap[2 * i + 1]))

    def minHeap(self):
        # Build the min-heap from an unordered array
        for pos in range(self.size // 2, 0, -1):
            self.minHeapify(pos)  

    def remove(self):
        # Remove and return the root (minimum element) of the heap
        popped = self.Heap[self.FRONT] 
        self.Heap[self.FRONT] = self.Heap[self.size]  
        self.size -= 1  
        self.minHeapify(self.FRONT) 
        return popped  

if __name__ == "__main__":
    print('The minHeap is ')
     # Create a MinHeap with a maximum size of 15
    minHeap = MinHeap(15) 
    minHeap.insert(5) 
    minHeap.insert(3)
    minHeap.insert(17)
    minHeap.insert(10)
    minHeap.insert(84)
    minHeap.insert(19)
    minHeap.insert(6)
    minHeap.insert(22)
    minHeap.insert(9)
    minHeap.minHeap()
# Print the heap structure
    minHeap.Print()  
    print("The Min val is " + str(minHeap.remove()))  




