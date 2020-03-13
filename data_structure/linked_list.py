# head is nothing but starting value
# dataval is nothing but data or to see the data of current element or
# next element we will use
# nextval is nothing but address of next element
# linked list is the sequence of data elements connected via data links
# each data element consists of link of another data element in the form of pointer.

# [head value ][pointing to next element ] --[data][pointing to next ]--[data][None]


class Node:

    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None


class SingleNodelist:

    def __init__(self):
        self.headval = None


list1 = SingleNodelist()
# Assigning the first value to head
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Linking the second node to first node
list1.headval.nextval = e2

# Linking the third node to second node
e2.nextval = e3


class Node:

    def __init__(self, dataval):
        self.dataval = dataval
        self.nextval = None


class SingleNode:

    def __init__(self):
        self.headval = None

    def display_elements(self):
        printval = self.headval
        while printval:
            print(printval.dataval)
            printval = printval.nextval

list1 = SingleNode()
# Assigning first value to head
list1.headval = Node("Monday")

e2 = Node("Tue")
e3 = Node("Wed")

# linking the second element to first element
list1.headval.nextval = e2

# linking the third element to secod element
e2.nextval = e3
list1.display_elements()


class Node:

    def __init__(self, dataval):
        self.dataval = dataval
        self.nextval = None

class SingleNode:

    def __init__(self):
        self.headval = None

    def display_nodes(self):
        printval = self.headval
        while printval:
            print(printval.dataval)
            printval = printval.nextval

    def adding_node_at_begining(self, newdata):
        newnode = Node(newdata)
        # keeping the node at begining
        newnode.nextval = self.headval
        self.headval = newnode

    def adding_element_at_end(self, newdata):
        newnode = Node(newdata)
        if not self.headval:
            self.headval = newnode
            return
        last = self.headval
        while (last.nextval):
            last = last.nextval
        last.nextval = newnode

    def adding_node_between_elements(self, middle, newdata):
        if not middle:
            print("the middle node is needed")
            return
        newnode = Node(newdata)
        newnode.nextval = middle.nextval
        middle.nextval = newnode

list1 = SingleNode()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("wed")

# linking the second node to first node
list1.headval.nextval = e2

# linking the third node to second node
e2.nextval = e3


#list1.adding_node_at_begining("sunday")
#list1.adding_element_at_end("thru")
list1.adding_node_between_elements(list1.headval.nextval, "sat")
list1.display_nodes()




class Node:

    def __init__(self, dataval):
        self.dataval = dataval
        self.nextval = None

class SingleNode:
    def __init__(self):
        self.headval = None

    def display_elements(self):
        element = self.headval
        while element:
            print(element.dataval)
            element = element.nextval

    def add_element_at_the_begining(self, new_value):
        new_object = Node(new_value)

        # assign next value  for new_object which is self.headval
        new_object.nextval = self.headval

        # assign given value to self.headval
        self.headval = new_object

    def add_element_at_the_ending(self, new_value):
        new_object_end = Node(new_value)

        if not self.headval:
            self.headval = new_object_end
            return
        # assigning headval as last
        last = self.headval
        while last.nextval:
            last =  last.nextval
        last.nextval = new_object_end




object = SingleNode()
object.headval = Node("one")
e2 = Node("two")
e3 = Node("three")

# assigning next element value to current point
object.headval.nextval = e2

# assigning next element value to current point
e2.nextval = e3

# display the values
# object.display_elements()

# [head value ][pointing to next element ] --[data][pointing to next ]--[data][None]

# add element at the begin
# we need to have one value let say four
#  create node object by using given variable
#  now assign node next value as head value
# now assign head value as given value
# [head value ][pointing to next element] -- [data][pointing to next element ] --[data][pointing to next ]--[data][None]

object.add_element_at_the_begining("four")
object.display_elements()


# check head_value is there or right
# if head value is there take that element as last element
# and if last element.nextval available treat that as last element
# after object.nextval = newnode

object.add_element_at_the_ending("five")
object.display_elements()