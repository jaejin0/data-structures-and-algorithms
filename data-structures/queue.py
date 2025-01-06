# queue is a First-In-First-Out (FIFO) data structure

class Queue:
    def __init__(self, array=[]):
        self.array = array
        self.front = 0
        self.rear = len(array) - 1

    def push(self, value):
        self.array.append(value)
        self.rear += 1

    def pop(self):
        self.rear -= 1
        self.array.pop(0)

    def get_front(self):
        return self.array[self.front]

    def get_rear(self):
        return self.array[self.rear]

    def print(self):
        print(self.array)

if __name__ == "__main__":
    queue = Queue([0, 1, 2, 3, 4])
    queue.push(5)
    queue.push(6)
    queue.print()
    queue.pop()
    queue.print()
    print(queue.get_front())
    print(queue.get_rear())
