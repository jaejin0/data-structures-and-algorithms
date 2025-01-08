# binary heap is a array to represent min-heap or max-heap

'''
root: array[0]

for ith node:
    ith node: array[i]
    parent node: array[(i - 1) / 2]
    left child node: array[(2 * i) + 1]
    right child node: array[(2 * i) + 2]
'''

class BinaryHeap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.heap = [0] * (self.maxsize + 1)
    
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
                self.heap[pose > self.heap[self.right_child(pos)]):

                if self.heap[self.left_child(pos)] < self.heap[self.right_child(pos)]:
                    self.swap(pos, self.left_child(pos))
                    self.heapify(self.left_child(pos))
                else:
                    self.swap(pos, self,right_child(pos))
                    self.heapify(self.right_child(pos))



    def getMin(self): # O(1)
        return self.array[0]

    def popMin(self): # O(log(n))
        pass

    def decreaseKey(self): # O(log(n))
        pass

    def insert(self, value): # O(log(n))
        pass

    def delete(self): # O(log(n))
        pass
