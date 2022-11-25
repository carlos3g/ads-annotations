from Node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, element):
        self._size += 1

        if (not self.head):
            self.head = Node(element)
            return

        pointer = self.head
        while (pointer.next):
            pointer = pointer.next
        pointer.next = Node(element)

    def insert(self, index, element):
        node = Node(element)
        self._size += 1

        if (index == 0):
            node.next = self.head
            self.head = node
            return

        pointer = self._get_node(index - 1)
        node.next = pointer.next
        pointer.next = node

    def remove(self, element):
        self._size -= 1

        if (self._size and self.head.data == element):
            self.head = self.head.next
            return True

        ancestor = self.head
        pointer = self.head.next
        while (pointer):
            if (pointer.data == element):
                ancestor.next = pointer.next
                pointer.next = None
                return True
            ancestor = pointer
            pointer = pointer.next

        raise ValueError(f'{element} is not in list')

    def index(self, element):
        pointer = self.head
        i = 0

        while (pointer):
            if (pointer.data == element):
                return i
            pointer = pointer.next
            i += 1

        raise ValueError(f'{element} is not in list')

    def _get_node(self, index):
        pointer = self.head
        for _ in range(index):
            if (pointer):
                pointer = pointer.next
                continue
            break

        if (pointer):
            return pointer

        raise IndexError('list index out of range')

    def __getitem__(self, index):
        return self._get_node(index).data

    def __setitem__(self, index, element):
        node = self._get_node(index)
        node.data = element

    def __delitem__(self, index):
        self._size -= 1

        if (index == 0):
            self.head = self.head.next
            return

        pointer = self._get_node(index - 1)
        pointer.next = pointer.next.next

    def __len__(self):
        return self._size

    def __repr__(self):
        repr = ''
        pointer = self.head

        while (pointer):
            repr += f'{str(pointer.data)} -> '
            pointer = pointer.next

        return repr

    def __str__(self):
        return self.__repr__()
