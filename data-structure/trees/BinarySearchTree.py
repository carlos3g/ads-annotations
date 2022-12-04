from Node import Node
from BinaryTree import BinaryTree


class BinarySearchTree(BinaryTree):
    def insert(self, value):
        parent = None
        x = self.root

        while (x):
            parent = x

            if (value < x.data):
                x = x.left
                continue

            x = x.right

        if (parent is None):
            self.root = Node(value)
            return

        if (value < parent.value):
            parent.left = Node(value)
            return

        parent.right = Node(value)

    def remove(self, value, node=0):
        if (node == 0):
            node = self.root

        if (node is None):
            return node

        if (value < node.data):
            node.left = self.remove(value, node.left)
        elif (value > node.data):
            node.right = self.remove(value, node.right)
        else:
            if (node.left is None):
                return node.right

            if (node.right is None):
                return node.left

            substitute = self.min(node.right)
            node.data = substitute
            node.right = self.remove(substitute, node.right)

        return node

    def search(self, value, node=0):
        if (node == 0):
            node = self.root

        if (node is None):
            return node

        if (node.data == value):
            return BinarySearchTree(None, node)

        if (value < node.data):
            return self.search(value, node.left)

        return self.search(value, node.right)

    def min(self, node=None):
        if (node is None):
            node = self.root

        while (node.left):
            node = node.left

        return node.data

    def max(self, node=None):
        if (node is None):
            node = self.root

        while (node.right):
            node = node.right

        return node.data
