# tree is a hierarchical structure used to represent data in parent child relationship

class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

class Tree:
    def __init__(self, node=None):
        self.root = node

    def print(self, root=None):
        root = self.root if root == None else root
        print(root.value)
        for node in root.children:
            self.print(node)


if __name__ == "__main__":
    child3 = Node(3)
    child4 = Node(4)
    child5 = Node(5)
    child6 = Node(6)

    child1 = Node(1, [child3, child4])
    child2 = Node(2, [child5, child6])

    root = Node(0, [child1, child2])
    
    tree = Tree(root)
    tree.print()
