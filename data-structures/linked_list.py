class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self, node: Node = None):
        self.head = node

    def insert(self, node: Node):
        if self.head == None:
            self.head = node
        else:
            cur_node = self.head
            while cur_node.next_node:
                cur_node = cur_node.next_node
            cur_node.next_node = node

    def print(self):
        if self.head == None:
            print("[]")
            return
        output = "["
        cur_node = self.head
        while cur_node:
            output += str(cur_node.value) + ", "
            cur_node = cur_node.next_node
        print(output.strip()[:-1] + "]")

if __name__ == "__main__":
    linkedlist = LinkedList()
    linkedlist.insert(Node(3))
    linkedlist.insert(Node(4))
    linkedlist.print()
