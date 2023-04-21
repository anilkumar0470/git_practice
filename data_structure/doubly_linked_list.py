# doubly linked list means one data with two pointers one is previous and another one is next

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def forward_traversal(self):
        if self.head is None:
            print("doubly linked list is empty")
        else:
            a = self.head
            while a is not None:
                print(a.data, end=" ")
                a = a.next

    def backward_traversal(self):
        if self.head is None:
            print("doubly linked list is empty")
        else:
            a = self.head
            while a.next is not None:
                a = a.next
            while a is not None:
                print(a.data, end=" ")
                a = a.prev

    def insertion_at_beginning(self, data):
        nb = Node(data)
        a = self.head
        a.prev = nb
        nb.next = a
        self.head = nb

    def insertion_at_end(self, data):
        ne = Node(data)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = ne
        ne.prev = a

    def insertion_at_specified_node(self, data, position):
        nm = Node(data)
        a = self.head
        for i in range(1, position-1):
             a = a.next
        nm.prev = a
        nm.next = a.next
        a.next.prev = nm
        a.next = nm

    def deletion_at_beginning(self):
        a = self.head
        self.head = a.next
        a.next = None
        self.head.prev = None

    def deletion_at_end(self):
        b = self.head
        a = self.head.next
        while a.next is not None:
            a = a.next
            b = b.next
        b.next = None
        a.prev = None

    def delete_at_specified_node(self, position):
        b = self.head
        a = self.head.next
        for i in range(1, position-1):
            a = a.next
            b = b.next
        b.next = a.next
        a.next.prev = b
        a.prev = None
        a.next = None


n1 = Node(5)
n2 = Node(10)
n3 = Node(15)
n4 = Node(25)
dll = DoublyLinkedList()
dll.head = n1
n1.next = n2
n1.prev = None
n2.next = n3
n2.prev = n1
n3.next = n4
n3.prev = n2
n4.prev = n3
dll.forward_traversal()
print()
dll.backward_traversal()
dll.insertion_at_beginning(1)
print()
dll.forward_traversal()
print()
dll.backward_traversal()
dll.insertion_at_specified_node(13,3)
print()
dll.forward_traversal()
dll.deletion_at_beginning()
print()
dll.forward_traversal()
dll.deletion_at_end()
print()
dll.forward_traversal()
dll.delete_at_specified_node(3)
print()
dll.forward_traversal()

