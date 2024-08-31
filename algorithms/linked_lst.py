from typing import Optional


class ListNode:

    def __init__(self, data = None) -> None:
        self.data = data
        self.next: Optional['ListNode'] = None


class LinkedList:

    def __init__(self) -> None:
        self.head = ListNode()

    def append(self, data):
        new = ListNode(data)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new

    def length(self):
        current = self.head
        total_length = 0
        while current.next is not None:
            total_length += 1
            current = current.next
        return total_length

    def display(self):
        elements = []
        current = self.head
        while current.next is not None:
            current = current.next
            elements.append(current.data)
        print(elements)

    def pop(self, index: int):
        if index >= self.length():
            raise IndexError('index out of range')
        current_index = 0
        current = self.head
        while current.next is not None:
            current = current.next
            if current_index == index:
                return current.data
            current_index += 1

    def erase(self, index: int):
        if index >= self.length():
            raise IndexError('index out of range')
        current_index = 0
        current = self.head
        while current.next is not None:
            previous = current
            current = current.next
            if current_index == index:
                previous.next = current.next
                return
            current_index += 1

    def remove_duplicates(self):
        current = self.head.next
        previous = self.head
        seen = set()
        while current:
            if current.data in seen:
                previous.next = current.next
            else:
                seen.add(current.data)
                previous = current
            current = current.next

    def remove_sorted_duplicates(self):
        current = self.head
        while current:
            while current.next and current.next.data == current.data:
                current.next = current.next.next
            current = current.next



my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(2)
my_list.append(2)
my_list.append(3)
my_list.append(4)

print("Before removing duplicates:")
my_list.display()

my_list.remove_sorted_duplicates()

print("After removing duplicates:")
my_list.display()
