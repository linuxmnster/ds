class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, new_value):
        if new_value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(new_value)
            else:
                self.left.insert(new_value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(new_value)
            else:
                self.right.insert(new_value)

    def inorder_traverse(self):
        if self.left:
            self.left.inorder_traverse()
        print(self.value, end=" ")
        if self.right:
            self.right.inorder_traverse()

bst = BinarySearchTree(10)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(7)

print("In-order traversal:")
bst.inorder_traverse()
