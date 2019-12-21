from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None # current oldest node
        self.storage = DoublyLinkedList()

    def append(self, item):



        # check current size, if below capacity, append, if equal capacity, remove oldest (the head), and add to tail
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
        else:
            # overwrite current  pointer
            self.current.value = item
            # increment the pointer
            if self.current is not self.storage.tail:
                self.current = self.current.next
            else:
                self.current = self.storage.head

        if self.storage.length == 1:
            self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        item = self.storage.head
        while item != None:
            list_buffer_contents.append(item.value)
            item = item.next


        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
