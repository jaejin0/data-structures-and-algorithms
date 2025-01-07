# expression tree is a binary tree which each internal node is operator and each leaf node is numbers

operators = {"+", "-", "*", "/"}
parenthesis = {"(", ")"}

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class ExpressionTree:
    def __init__(self, root):
        self.root = root

    def print(self, root=None):
        root = self.root if root == None else root
        print(root.value)
        for node in root.children:
            self.print(node)

def solve_expression_tree(expresion_tree):
    
    def recursion(root):
        print(root.value)
        if root.value in operators:
            match root.value:
                case "+":
                    return recursion(root.left) + recursion(root.right)
                case "-":
                    return recursion(root.left) - recursion(root.right)
                case "*":
                    return recursion(root.left) * recursion(root.right)
                case "/":
                    return recursion(root.left) / recursion(root.right)
        else:
            return root.value

    return recursion(expression_tree.root)

if __name__ == "__main__":
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    node1 = Node("+", node3, node4)
    node2 = Node("+", node5, node6)

    node0 = Node("+", node1, node2)

    expression_tree = ExpressionTree(node0)

    print(solve_expression_tree(expression_tree)) 

