from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Check if the length is equal to the capacity to keep it from going over max capacity
        # If it's less than capacity just add the item to the tail
        # If it's equal to the capacity remove the head (oldest value) and add the new one to the tail (a queue)
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        else:
            to_delete = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if to_delete == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        # Start with the current value
        # If Next is none, use the head instead (this is how the 'ring' works)
        # Go through the list and as long sa the next node isn't the same as the initial node (or None) append the value
        initial = self.current
        list_buffer_contents.append(initial.value)

        if initial.next is not None:
            next_node = initial.next
        else:
            next_node = self.storage.head

        while next_node != initial:
            list_buffer_contents.append(next_node.value)
            if next_node.next is not None:
                next_node = next_node.next
            else:
                next_node = self.storage.head

        return list_buffer_contents

# ----------------Stretch Goal-------------------

# MVP can be done with a singly linked list. Since a doubly linked list is imported, will that be useful here?

class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
