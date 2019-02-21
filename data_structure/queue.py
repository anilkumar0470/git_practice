class Queue:

    def __init__(self):
        self.queue = []

    def adding_element_to_queue(self, data_element):
        if data_element not in self.queue:
            self.queue.insert(0, data_element)
            return True
        return False

    def length_of_queue(self):
        return len(self.queue)

    def remove_element_from_queue(self):
        if len(self.queue) > 0 :
           return self.queue.pop()
        return "No elements found in stack"


q = Queue()
q.adding_element_to_queue("Sun")
q.adding_element_to_queue("Mon")
q.adding_element_to_queue("Tue")
print(q.length_of_queue())
q.remove_element_from_queue()
print(q.length_of_queue())