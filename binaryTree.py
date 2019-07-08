# learnig how to create an binary tree


class BinaryTree:
    def __init__(self, root):
        self.left = None
        self.right = None
        self.root = root

    def getLeft(self): return self.left

    def getRight(self): return self.right

    def setRoot(self, value): self.root = value

    def getRoot(self): return self.root

    def insertRight(self, node):
        if self.right is None:
            self.right = BinaryTree(node)
        else:
            tree = BinaryTree(node)
            tree.right = self.right
            self.right = tree

    def insertLeft(self, node):
        if self.left is None:
            self.left = BinaryTree(node)
        else:
            tree = BinaryTree(node)
            tree.left = self.left
            self.left = tree


def printTree(tree):
    if tree is not None:
        printTree(tree.getLeft())  # Recursive case
        print(tree.getRoot())
        printTree(tree.getRight())  # recursive case


if __name__ == "__main__":
    myTree = BinaryTree("Gigi")
    myTree.insertLeft("Bob")
    myTree.insertRight("Cata")
    myTree.insertRight("Madalina")

    printTree(myTree)
