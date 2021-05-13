# stack means arranging the elements one over another
# LIFO the element which come last is removed first

class Stack:

    def __init__(self):
        self.stack = []

    def add_elements_to_stack(self, element):
        if element not in self.stack:
            self.stack.append(element)
            return True
        else:
            return False

    # used to display the top element of stack i.e first element
    def peek(self):
        return self.stack[-1]

    def remove_element_from_stack(self):
        if len(self.stack) <= 0:
            return "no elements available in stack"
        else:
            return self.stack.pop()


s = Stack()
s.add_elements_to_stack("Mon")
s.add_elements_to_stack("Tue")
print (s.peek())
s.add_elements_to_stack("Wed")
s.add_elements_to_stack("Thu")
print (s.peek())
print (s.stack)
s.remove_element_from_stack()
print (s.stack)


class Stack:

    def __init__(self):
        self.stack = []

    def add_element_to_stack(self, element):

        if element not in self.stack:
            self.stack.append(element)
            return True
        else:
            return False

    def remove_element_from_stack(self):
        if len(self.stack) <= 0 :
            return  ("no elements found in the stack")
        else:
            return self.stack.pop()
    def peek_element(self):
        print(self.stack[-1])

stack_object = Stack()
stack_object.add_element_to_stack(1)
stack_object.add_element_to_stack(2)
stack_object.add_element_to_stack(3)
print(stack_object.remove_element_from_stack())


sad = '[5e8c4b740a61e04edc079180, 5e8c4b740a61e04edc079181]'

s = ""
l = []

for i in sad:
    if i.isalnum():
        s = s + i
    else:
        if s :
            l.append(s)
            s = ""
print(l)

class NewStack:

    def __init__(self):
        self.stack = []

    def add_element_into_stack(self, element):
        if element not in self.stack:
            self.stack.append(element)
            return True
        else:
            return False

    def remove_element_from_stack(self):
        if len(self.stack) <=0:
            print("no elements in the stack")
        return self.stack.pop()

    def display_peek_element(self):
        if len(self.stack) >0:
            return self.stack[-1]


new = NewStack()
new.add_element_into_stack("MON")
# print(new.display_peek_element())
new.add_element_into_stack("TUE")
print(new.display_peek_element())



