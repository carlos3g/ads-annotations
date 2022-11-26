from Node import Node


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def push(self, element):
        node = Node(element)
        self._size += 1

        if (not self._size):
            self.first = node
            self.last = node
            return

        self.last.next = node
        self.last = node

    def pop(self):
        if (self._size):
            node = self.first
            self.first = self.first.next
            self._size -= 1
            return node.data

        raise IndexError('The queue is empty')

    def peek(self):
        if (self._size):
            return self.first.data

        raise IndexError('The queue is empty')

    def __len__(self):
        return self._size

    def __repr__(self):
        repr = ''
        pointer = self.top

        while (pointer):
            repr += f'{str(pointer.data)} ->  '
            pointer = pointer.next

        return repr

    def __str__(self):
        return self.__repr__()
