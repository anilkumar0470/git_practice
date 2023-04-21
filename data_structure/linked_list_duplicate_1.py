# # class Node:
# #
# #     def __init__(self, data=None):
# #         self.dataval = data
# #         self.next_value = None
# #
# #
# # class SingleNode:
# #
# #     def __init__(self):
# #         self.headval = None
# #
# #     def display_elements(self):
# #         element = self.headval
# #         while element:
# #             print(element.dataval)
# #             element = element.next_value
# #
# #     def add_element_at_begining(self, new_element):
# #         new_element_object = Node(new_element)
# #
# #         # linking the new element link to head value
# #         new_element_object.next_value = self.headval
# #         self.headval = new_element_object
# #
# #     def add_element_add_end(self, new_element):
# #         new_node = Node(new_element)
# #
# #         #checking first value or head value
# #         if self.headval is None:
# #             self.headval = new_node
# #             return
# #         last_element = self.headval
# #         while (last_element.next_value):
# #             last_element = last_element.next_value
# #         last_element.next_value = new_node
# #
# #     def add_in_between(self, middle_node, element):
# #         if middle_node is None:
# #             print("The mentioned node is absent ")
# #             return
# #         new_node = Node(element)
# #         new_node.next_value = middle_node.next_value
# #         middle_node.next_value = new_node
# #
# #
# #
# # object1 = SingleNode()
# # object1.headval  = Node("1One")
# # e2 = Node("2Two")
# # e3 = Node("3Three")
# #
# # # assigning next value to current element
# # object1.headval.next_value = e2
# # # assigning next value to current element
# # e2.next_value = e3
# #
# # object1.add_element_at_begining("4four")
# # object1.add_element_add_end("5five")
# # object1.add_in_between(e3, "6six")
# # object1.display_elements()
# #
# # list = [1,2,3,3,2,4,5,6,4]
# # result=[v for i,v in enumerate(list) if v not in list[:i]]
# # print(result)
#
#
# #importing module
# import logging
#
# #Create and configure logger
# logging.basicConfig(filename="newfile.log",
# 					format='%(asctime)s %(message)s',
# 					filemode='w')
#
# #Creating an object
# logger=logging.getLogger()
#
# #Setting the threshold of logger to DEBUG
# logger.setLevel(logging.INFO)
#
# #Test messages
# logger.debug("Harmless debug Message")
# logger.info("Just an information")
# logger.warning("Its a Warning")
# logger.error("Did you try to divide by zero")
# logger.critical("Internet is down")
#
# class Node:
#
# 	def __init__(self, data):
# 		self.data = data
# 		self.next = None
#
#
# class SingleLinkedList:
#
# 	def __init__(self):
# 		self.head = None
#
# 	def traversing_in_linked_list(self):
# 		element = self.head
# 		while element:
# 			print(element.data)
# 			element = element.next
#
# 	def insert_at_beginning(self, item_to_insert):
# 		n0 = Node(item_to_insert)
# 		n0.next = self.head
# 		self.head = n0
#
# 	def insert_at_the_end(self, item_to_insert):
# 		ne = Node(item_to_insert)
# 		a = self.head
# 		while a.next is not None:
# 			a = a.next
# 		a.next = ne
#
# 	def insertion_at_specified_position(self, item, position):
# 		ns = Node(item)
# 		a = self.head
# 		for i in range(1, position-1):
# 			a = a.next
# 		ns.next = a.next
#
#
#
#
#
#
#
# sll = SingleLinkedList()
# n1 = Node("monday")
# sll.head = n1
#
# n2 = Node("tue")
# n1.next = n2
# n3 = Node("wed")
# n2.next = n3
#
# sll.insert_at_beginning("sun")
# sll.insert_at_beginning("sat")
# sll.traversing_in_linked_list()
# sll.insert_at_the_end("thur")
# sll.traversing_in_linked_list()
#

# linked list is a linear data structure
# it is collection of nodes and each node contain data and reference/next
# it is more efficient then list/array with respect to insert/delete
# node will always contains data and reference and head always point to first node

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


# class SingleLinkedList:
# 	def __init__(self):
# 		self.head = None
#
# 	def traversal(self):
# 		if self.head is None:
# 			print("single linked list is empty")
# 		else:
# 			a = self.head
# 			while a:
# 				print(a.data, end=" ")
# 				a = a.next
#
# 	def insertion_at_begging(self, data):
# 		print()
# 		nb = Node(data)
# 		nb.next = self.head
# 		self.head = nb
#
# 	def insertion_at_end(self, data):
# 		print()
# 		ne = Node(data)
# 		a = self.head
# 		while a.next:
# 			a = a.next
# 		a.next = ne
#
# 	def insertion_at_specified_node(self, data, position):
# 		print()
# 		ns = Node(data)
# 		a = self.head
# 		for i in range(1, position-1):
# 			a = a.next
# 		ns.next = a.next
# 		a.next = ns
#
#
#
#
#
#
#
#
# n1 = Node(5)
# sl = SingleLinkedList()
# sl.traversal()
# sl.head = n1
#
# n2 = Node(10)
# n1.next = n2
#
# n3 = Node(15)
# n2.next = n3
#
# n4 = Node(20)
# n3.next = n4
# sl.traversal()
#
# # insertion at beginning
# sl.insertion_at_begging(1)
# sl.traversal()
#
# # insertion at end
# sl.insertion_at_end(25)
# sl.traversal()
#
# # insertion at specified node
# sl.insertion_at_specified_node(12, 4)
# sl.traversal()
#
# class Node:
# 	def __init__(self, data):
# 		self.data = data
# 		self.next = None
#
#
# class SingleLinked:
# 	def __init__(self):
# 		self.head = None
#
# 	def travasel(self):
#
# 		if self.head is None:
# 			# print()
# 			print("linked list is empty")
# 		else:
# 			a = self.head
# 			while a:
# 				print(a.data, end=" ")
# 				a = a.next
#
# 	def insert_at_beginning(self, data):
# 		nb = Node(data)
# 		nb.next = self.head
# 		self.head = nb
#
# 	def insert_at_end(self, data):
# 		ne = Node(data)
# 		a = self.head
# 		while a.next is not None:
# 			a = a.next
# 		a.next = ne
#
# 	def insert_at_specified_node(self, data, position):
# 		nsp = Node(data)
# 		a = self.head
# 		for i in range(1, position-1):
# 			a = a.next
# 		nsp.next = a.next
# 		a.next = nsp
#
# 	def get_length_of_linked_list(self):
# 		a = self.head
# 		count = 0
# 		while a:
# 			count += 1
# 			a = a.next
# 		return count
#
# 	def print_middle_element(self):
# 		a = self.head
# 		length = self.get_length_of_linked_list()
# 		mid_index = length//2
# 		while mid_index:
# 			a = a.next
# 			mid_index = mid_index - 1
# 		print("mid value is {}".format(a.data))
#
#
#
# n1 = Node(10)
# sl = SingleLinked()
# sl.travasel()
# sl.head = n1
# n2 = Node(20)
# n1.next = n2
# n3 = Node(30)
# n2.next = n3
# n4 = Node(40)
# n3.next = n4
# sl.travasel()
# sl.insert_at_beginning(5)
# sl.travasel()
# sl.insert_at_end(50)
# sl.travasel()
# sl.insert_at_specified_node(90, 4)
# sl.travasel()
# print()
# print(sl.get_length_of_linked_list())
# sl.print_middle_element()
# sl.insert_at_end(1)
# sl.travasel()
# print()
# sl.print_middle_element()
