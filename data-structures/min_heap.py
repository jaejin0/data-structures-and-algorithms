# min heap is a binary heap to easily get minimum value 

'''
root: array[0]

for ith node:
    ith node: array[i]
    parent node: array[(i - 1) / 2]
    left child node: array[(2 * i) + 1]
    right child node: array[(2 * i) + 2]
'''

class MinHeap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.heap = [0] * (self.max_size + 1)
        self.Heap[0] = float('-inf')
        self.FRONT = 1

    def parent(self, pos):
        return pos//2

    def left_child(self, pos):
        return 2 * pos

    def right_child(self, pos):
        return (2 * pos) + 1

    def is_leaf(self, pos):
        return pos*2 > self.size

    def swap(self, pos1, pos2):
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]

    def heapify(self, pos):
        
        if not self.is_leaf(pos):
            if (self.heap[pos] > self.heap[self.left_child(pos)] or
                self.heap[pos] > self.heap[self.right_child(pos)]):

                if self.heap[self.left_child(pos)] < self.heap[self.right_child(pos)]:
                    self.swap(pos, self.left_child(pos))
                    self.heapify(self.left_child(pos))
                else:
                    self.swap(pos, self,right_child(pos))
                    self.heapify(self.right_child(pos))

    def insert(self, value): # O(log(n))
        if self.size >= self.max_size:
            return
        self.size += 1
        self.heap[self.size] = value

        cur = self.size
        while self.heap[cur] < self.heap[self.parent(cur)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def Print(self):
        for i in range(0, (self.size // 2) + 1):
            print(" PARENT : " + str(self.heap[i]) + 
                  " LEFT CHILD : " + str(self.heap[2 * i]) + 
                  " RIGHT CHILD : " + str(self.heap[2 * i + 1]))

    def min_heap(self):
        for pos in range(self.size // 2, 0, -1):
            self.heapify(pos)

    def remove(self):
        popped = self.heap[self.FRONT]
        self.heap[self.FRONT] = self.heap[self.size]
        self.size -= 1
        self.minheapify(self.FRONT)
        return popped

if __name__ == "__main__": 
      
    print('The minHeap is ') 
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
  
    minHeap.Print() 
    print("The Min val is " + str(minHeap.remove())) 
