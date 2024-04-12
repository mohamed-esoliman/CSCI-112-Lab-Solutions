"""
Author: Mohamed Soliman
File: linkedlist.py
"""


class Node(object):
    """Represents a singly linked node."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    """Represents a linked list."""

    def __init__(self, sourceCollection=None):
        """Creates a linked list."""
        self.head = None
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def __len__(self):
        """Returns the number of items in the linked list."""
        return self.size

    def __contains__(self, item):
        """Determines if the given item is in the linked list."""
        current = self.head
        while current is not None and current.data != item:
            current = current.next
        return current is not None

    def add(self, item):
        """Adds the given item to the linked list."""
        self.head = Node(item, self.head)
        self.size += 1

    def remove(self, item):
        """Removes the given item from the linked list."""
        previous = None
        current = self.head
        while current is not None and current.data != item:
            previous = current
            current = current.next
        if current is not None:
            self.size -= 1
            if current is self.head:
                self.head = current.next
            else:
                previous.next = current.next
            return True
        return False

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self.head
        while cursor is not None:
            yield cursor.data
            cursor = cursor.next

    def __str__(self):
        """Returns the string representation of the linked list."""
        return "[" + ", ".join(map(str, self)) + "]"

    def __add__(self, other):
        """Returns a new linked list containing the contents of self and other."""
        result = LinkedList(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """Determines if self equals other."""
        if self is other:
            return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        for i in self:
            for j in other:
                if not i == j:
                    return False
        return True


def main():
    """Tests the LinkedList class."""
    lyst = LinkedList()
    for item in range(5, 0, -1):
        lyst.add(item)
    print("Expect 5:", len(lyst))
    print("Expect the items on separate lines:")
    for item in lyst:
        print(item)
    print("Expect True:", 3 in lyst)
    print("Expect False:", 6 in lyst)
    lyst.remove(3)
    print("Expect 4:", len(lyst))
    print("Expect the items on separate lines:")
    for item in lyst:
        print(item)


if __name__ == "__main__":
    main()
