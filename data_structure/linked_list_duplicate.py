class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SingleLink:

    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval:
            print (printval.dataval)
            printval = printval.nextval


# s = SingleLink()
# s.headval = Node("Mon")
# e2 = Node("Tue")
# e3 = Node("Wed")
#
# # linking the first node to second node
# s.headval.nextval = e2
# # linking the second node to third node
# e2.nextval = e3
# s.listprint()

# inserting elements into linked list
# inserting the data elemeents involves the reassiging of pointers of existing node
# to newly created node
# inserting at the begining

class Node:

    def __init__(self, data=None):
        self.data = data
        self.nextval = None


class SingleLink:

    def __init__(self):
        self.headval = None

    def listelements(self):
        printval = self.headval
        while printval:
            print (printval.data)
            printval = printval.nextval

    def inserting_element_at_begining(self, newdata):
        newnode = Node(newdata)

        # updating new node as first node

        newnode.nextval = self.headval
        self.headval = newnode
# s = SingleLink()
# s.headval = Node("Mon")
# e2 = Node("Tue")
# e3 = Node("Wed")
#
# # linking the first element to second element
# s.headval.nextval = e2
#
# # linking the second element to third element
# e2.nextval = e3
# #s.listelements()
# s.inserting_element_at_begining("SUn")
# s.listelements()


# Inserting at the end of linked list
# to make this we need to assign the new data as current last node next val


class Node:

    def __init__(self, data = None):
        self.data = data
        self.nextval = None

class SingleLinked:

    def __init__(self):
        self.headval = None

    def display_elements(self):
        printval = self.headval
        while printval:
            print(printval.data)
            printval = printval.nextval

    def insert_at_end(self,newdata):
        new_node = Node(newdata)
        if self.headval is None:
            self.headval = new_node
            return
        laste = self.headval
        while laste.nextval:
            laste = laste.nextval
        laste.nextval = new_node


s = SingleLinked()
s.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# linking the first element to the second element
s.headval.nextval = e2

# linking the second node to third node
e2.nextval = e3

s.insert_at_end("Thu")
s.display_elements()

