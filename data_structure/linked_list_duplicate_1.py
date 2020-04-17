# class Node:
#
#     def __init__(self, data=None):
#         self.dataval = data
#         self.next_value = None
#
#
# class SingleNode:
#
#     def __init__(self):
#         self.headval = None
#
#     def display_elements(self):
#         element = self.headval
#         while element:
#             print(element.dataval)
#             element = element.next_value
#
#     def add_element_at_begining(self, new_element):
#         new_element_object = Node(new_element)
#
#         # linking the new element link to head value
#         new_element_object.next_value = self.headval
#         self.headval = new_element_object
#
#     def add_element_add_end(self, new_element):
#         new_node = Node(new_element)
#
#         #checking first value or head value
#         if self.headval is None:
#             self.headval = new_node
#             return
#         last_element = self.headval
#         while (last_element.next_value):
#             last_element = last_element.next_value
#         last_element.next_value = new_node
#
#     def add_in_between(self, middle_node, element):
#         if middle_node is None:
#             print("The mentioned node is absent ")
#             return
#         new_node = Node(element)
#         new_node.next_value = middle_node.next_value
#         middle_node.next_value = new_node
#
#
#
# object1 = SingleNode()
# object1.headval  = Node("1One")
# e2 = Node("2Two")
# e3 = Node("3Three")
#
# # assigning next value to current element
# object1.headval.next_value = e2
# # assigning next value to current element
# e2.next_value = e3
#
# object1.add_element_at_begining("4four")
# object1.add_element_add_end("5five")
# object1.add_in_between(e3, "6six")
# object1.display_elements()
#
# list = [1,2,3,3,2,4,5,6,4]
# result=[v for i,v in enumerate(list) if v not in list[:i]]
# print(result)


#importing module
import logging

#Create and configure logger
logging.basicConfig(filename="newfile.log",
					format='%(asctime)s %(message)s',
					filemode='w')

#Creating an object
logger=logging.getLogger()

#Setting the threshold of logger to DEBUG
logger.setLevel(logging.INFO)

#Test messages
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")
