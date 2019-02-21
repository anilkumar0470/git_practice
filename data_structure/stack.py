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
        return self.stack[0]

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