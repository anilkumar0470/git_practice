# head is nothing but starting value
# dataval is nothing but data or to see the data of current element or
# next element we will use
# nextval is nothing but address of next element
# linked list is the sequence of data elements connected via data links
# each data element consists of link of another data element in the form of pointer.


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

#linking the second element to first element
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







