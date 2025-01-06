# stack is a Last-In-First-Out (LIFO) data structure

class Stack:
    def __init__(self, array=[]):
        self.array = array
        self.top_index = -1 if array == [] else len(array) - 1

    def push(self, value):
        self.array.append(value)
        self.top_index += 1

    def top(self):
        return self.array[self.top_index]

    def pop(self):
        output = self.top()
        self.array.pop()
        self.top_index -= 1
        return output

    def print(self):
        print(self.array)
    
if __name__ == "__main__":
    stack = Stack([0, 1, 2])
    stack.push(3)
    stack.push(4)
    stack.print()
    stack.pop()
    print(stack.top())
