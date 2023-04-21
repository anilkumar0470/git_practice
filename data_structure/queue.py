# FIFO - first in first out
# enqueue -- inserting into element
# dequeue -- removing element from the queue
# display all elements in the queue
# inserting will happen at rear end and deletion will happen at front end
# class Queue:
#
#     def __init__(self):
#         self.queue = []
#
#     def adding_element_to_queue(self, data_element):
#         if data_element not in self.queue:
#             self.queue.insert(0, data_element)
#             return True
#         return False
#
#     def length_of_queue(self):
#         return len(self.queue)
#
#     def remove_element_from_queue(self):
#         if len(self.queue) > 0 :
#            return self.queue.pop()
#         return "No elements found in stack"
#
#
# q = Queue()
# q.adding_element_to_queue("Sun")
# q.adding_element_to_queue("Mon")
# q.adding_element_to_queue("Tue")
# print(q.length_of_queue())
# q.remove_element_from_queue()
# print(q.length_of_queue())


class NewQueue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        if item not in self.queue:
            self.queue.append(item)
            return True
        else:
            return False

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)

    def display_all_elements_in_queue(self):
        if len(self.queue) > 0:
            return self.queue

    def display_size_of_queue(self):
        return len(self.queue)


new_queue = NewQueue()
print(new_queue.display_size_of_queue())
new_queue.enqueue("customer 1")
print(new_queue.display_all_elements_in_queue())
new_queue.enqueue("customer2")
new_queue.enqueue("customer3")
new_queue.enqueue("customer4")
print(new_queue.display_all_elements_in_queue())
print(new_queue.display_size_of_queue())
print(new_queue.dequeue())
print(new_queue.display_all_elements_in_queue())