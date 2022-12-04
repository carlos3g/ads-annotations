from Node import Node
from ..queue.Queue import Queue


class BinaryTree:
    def __init__(self, data=None, node=None):
        if (node):
            self.root = node
            return

        if (data):
            self.root = Node(data)
            return

        self.root = data

    def inorder_traversal(self, node=None):
        if (node is None):
            node = self.root

        if (node.left):
            self.simetric_traversal(node.left)

        print(node, end=' ')

        if (node.right):
            self.simetric_traversal(node.right)

    def postorder_traversal(self, node=None):
        if (node is None):
            node = self.root

        if (node.left):
            self.postorder_traversal(node.left)

        if (node.right):
            self.postorder_traversal(node.right)

        print(node)

    def levelorder_traversal(self, node=None):
        if (node is None):
            node = self.root

        queue = Queue()
        queue.push(node)

        while (len(queue)):
            node = queue.pop()

            if (node.left):
                queue.push(node.left)

            if (node.right):
                queue.push(node.right)

            print(node, end=" ")

    def height(self, node=None):
        if (node is None):
            node = self.root

        hleft = hright = 0

        if (node.left):
            hleft = self.height(node.left)

        if (node.right):
            hright = self.height(node.right)

        if (hright > hleft):
            return hright + 1

        return hleft + 1
