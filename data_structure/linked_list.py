# # head is nothing but starting value
# # dataval is nothing but data or to see the data of current element or
# # next element we will use
# # nextval is nothing but address of next element
# # linked list is the sequence of data elements connected via data links
# # each data element consists of link of another data element in the form of pointer.
#
# # for first we dont have address
# # node contain two things one is data and another one is address of next node
# # for the last node we will have only data
#
# # [head value ][pointing to next element ] --[data][pointing to next ]--[data][None]
# # operations insertion -- beginning , at specified point, ending
# #            deletion -- beginning , at specified point, ending
# # traversal -- go through all elements one by one
# # always remember if you are inserting any value any where we need to do following things
# #
#
# class Node:
#
#     def __init__(self, dataval = None):
#         self.dataval = dataval
#         self.nextval = None
#
#
# class SingleNodelist:
#
#     def __init__(self):
#         self.headval = None
#
#
# list1 = SingleNodelist()
# # Assigning the first value to head
# list1.headval = Node("Mon")
# e2 = Node("Tue")
# e3 = Node("Wed")
#
# # Linking the second node to first node
# list1.headval.nextval = e2
#
# # Linking the third node to second node
# e2.nextval = e3
#
#
# class Node:
#
#     def __init__(self, dataval):
#         self.dataval = dataval
#         self.nextval = None
#
#
# class SingleNode:
#
#     def __init__(self):
#         self.headval = None
#
#     def display_elements(self):
#         printval = self.headval
#         while printval:
#             print(printval.dataval)
#             printval = printval.nextval
#
# list1 = SingleNode()
# # Assigning first value to head
# list1.headval = Node("Monday")
#
# e2 = Node("Tue")
# e3 = Node("Wed")
#
# # linking the second element to first element
# list1.headval.nextval = e2
#
# # linking the third element to secod element
# e2.nextval = e3
# list1.display_elements()
#
#
# class Node:
#
#     def __init__(self, dataval):
#         self.dataval = dataval
#         self.nextval = None
#
# class SingleNode:
#
#     def __init__(self):
#         self.headval = None
#
#     def display_nodes(self):
#         printval = self.headval
#         while printval:
#             print(printval.dataval)
#             printval = printval.nextval
#
#     def adding_node_at_begining(self, newdata):
#         newnode = Node(newdata)
#         # keeping the node at begining
#         newnode.nextval = self.headval
#         self.headval = newnode
#
#     def adding_element_at_end(self, newdata):
#         newnode = Node(newdata)
#         if not self.headval:
#             self.headval = newnode
#             return
#         last = self.headval
#         while (last.nextval):
#             last = last.nextval
#         last.nextval = newnode
#
#     def adding_node_between_elements(self, middle, newdata):
#         if not middle:
#             print("the middle node is needed")
#             return
#         newnode = Node(newdata)
#         newnode.nextval = middle.nextval
#         middle.nextval = newnode
#
# list1 = SingleNode()
# list1.headval = Node("Mon")
# e2 = Node("Tue")
# e3 = Node("wed")
#
# # linking the second node to first node
# list1.headval.nextval = e2
#
# # linking the third node to second node
# e2.nextval = e3
#
#
# #list1.adding_node_at_begining("sunday")
# #list1.adding_element_at_end("thru")
# list1.adding_node_between_elements(list1.headval.nextval, "sat")
# list1.display_nodes()
#
#
# class Node:
#
#     def __init__(self, dataval):
#         self.dataval = dataval
#         self.nextval = None
#
# class SingleNode:
#     def __init__(self):
#         self.headval = None
#
#     def display_elements(self):
#         element = self.headval
#         while element:
#             print(element.dataval)
#             element = element.nextval
#
#     def add_element_at_the_begining(self, new_value):
#         new_object = Node(new_value)
#
#         # assign next value  for new_object which is self.headval
#         new_object.nextval = self.headval
#
#         # assign given value to self.headval
#         self.headval = new_object
#
#     def add_element_at_the_ending(self, new_value):
#         new_object_end = Node(new_value)
#
#         if not self.headval:
#             self.headval = new_object_end
#             return
#         # assigning headval as last
#         last = self.headval
#         while last.nextval:
#             last =  last.nextval
#         last.nextval = new_object_end
#
#
#
#
# object = SingleNode()
# object.headval = Node("one")
# e2 = Node("two")
# e3 = Node("three")
#
# # assigning next element value to current point
# object.headval.nextval = e2
#
# # assigning next element value to current point
# e2.nextval = e3
#
# # display the values
# # object.display_elements()
#
# # [head value ][pointing to next element ] --[data][pointing to next ]--[data][None]
#
# # add element at the begin
# # we need to have one value let say four
# #  create node object by using given variable
# #  now assign node next value as head value
# # now assign head value as given value
# # [head value ][pointing to next element] -- [data][pointing to next element ] --[data][pointing to next ]--[data][None]
#
# object.add_element_at_the_begining("four")
# object.display_elements()
#
#
# # check head_value is there or right
# # if head value is there take that element as last element
# # and if last element.nextval available treat that as last element
# # after object.nextval = newnode
#
# object.add_element_at_the_ending("five")
# object.display_elements()
#
#

#
# # linked list implementation
# # a  node consist of data and reference to next data
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class SingleLinkedList:
#     def __init__(self):
#         self.head = None
#
#     def traversal_the_linked_list(self):
#
#         if self.head == None:
#             print("linked list is empty")
#         else:
#             a = self.head
#             while a is not None:
#                 print(a.data, end=" ")
#                 a = a.next
#
#     def insertion_at_beginning(self, data):
#         nb = Node(data)
#         nb.next = self.head
#         self.head = nb
#
#     def insertion_at_end(self, data):
#         ne = Node(data)
#         a = self.head
#         while a.next is not None:
#             a = a.next
#         a.next = ne
#
#     def insertion_at_specified_end(self, position, data):
#         ise = Node(data)
#         a = self.head
#         for i in range(1, position-1):
#             a = a.next
#         ise.next = a.next
#         a.next = ise
#
#     def delete_at_beginning(self):
#         a = self.head
#         self.head = a.next
#         a.next = None
#
#     def delete_at_the_end(self):
#         prev = self.head
#         a  = self.head.next
#
#         # while
#
#
#
# n1 = Node(10)
# sll = SingleLinkedList()
# sll.head = n1
# n2 = Node(20)
# n1.next = n2
# n3 = Node(30)
# n2.next = n3
# n4 = Node(40)
# n3.next = n4
# sll.traversal_the_linked_list()
# sll.insertion_at_beginning(5)
# print()
# sll.traversal_the_linked_list()
# sll.insertion_at_end(60)
# print()
# sll.traversal_the_linked_list()
# sll.insertion_at_specified_end(3, 33)
# print()
# sll.traversal_the_linked_list()
# sll.delete_at_beginning()
# print()
# sll.traversal_the_linked_list()

# data and address of next element
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class SingleLL:
#     def __init__(self):
#         self.head = None
#
#     def traversal(self):
#         a = self.head
#         while a is not None:
#             print(a.data, end=" ")
#             a = a.next
#
#
# n1 = Node(5)
# n2 = Node(10)
# n3 = Node(15)
# n4 = Node(20)
# sll = SingleLL()
# sll.head = n1
# n1.next = n2
# n2.next = n3
# n3.next = n4
# sll.traversal()
# nb = Node(2)

# insertion at beginning

# data, next, head

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def traversal(self):
        if self.head is None:
            return "linked list is empty"
        else:
            a = self.head
            while a is not None:
                print(a.data, end=" ")
                a = a.next

    def insert_at_beginning(self, value):
        nb = Node(value)
        nb.next = self.head
        self.head = nb

    def insert_at_end(self, value):
        ne = Node(value)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = ne

    def insert_at_specified_node(self, position, value):
        nm = Node(value)
        a = self.head
        for i in range(1, position):
            a = a.next
        nm.next = a.next
        a.next = nm

    def delete_at_beginning(self):
        a = self.head
        self.head = a.next
        a.next = None

    def delete_at_end(self):
        prev = self.head
        a = self.head.next
        while a.next is not None:
            a = a.next
            prev = prev.next
        prev.next =None

    def delete_at_specified_position(self, position):
        prev = self.head
        a = self.head.next
        for i in range(1, position):
            a = a.next
            prev = prev.next
        prev.next = a.next
        a.next = None


sll = SingleLinkedList()
n1 = Node(5)
n2 = Node(10)
n3 = Node(15)
n4 = Node(20)
sll.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
sll.traversal()
sll.insert_at_beginning(1)
print("insert at beginning ")
sll.traversal()

sll.insert_at_end(30)
print("insert at end")
sll.traversal()
sll.insert_at_specified_node(3, 25)
print("insert at specified node")
sll.traversal()
sll.delete_at_beginning()
print("delete at beginning")
sll.traversal()
sll.delete_at_end()
print("delete at the end")
sll.traversal()
sll.delete_at_specified_position(3)
print("delete at specified node")
sll.traversal()



















