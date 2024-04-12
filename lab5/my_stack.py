"""
Author: Mohamed Soliman
File: stack.py
"""

from node import Node


class Stack:
    """Represents a stack."""

    def __init__(self, sourceCollection=None):
        """Creates an empty stack."""
        self.top = None
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.push(item)

    def __len__(self):
        """Returns the number of items in the stack."""
        return self.size

    def __str__(self):
        """Returns the string representation of the stack."""
        return "[" + ", ".join(map(str, self)) + "]"

    def __iter__(self):
        """Supports iteration over a view of self."""
        # user should not need to iterate over the stack, but I added that to be able to use the __str__ in debugging
        cursor = self.top
        while cursor is not None:
            yield cursor.data
            cursor = cursor.next

    def __contains__(self, item):
        """Determines if the given item is in the stack."""
        for i in self:
            if i == item:
                return True
        return False

    def isEmpty(self):
        """Returns True if the stack is empty or False otherwise."""
        return self.top is None

    def push(self, data):
        """Adds the given data to the top of the stack."""
        self.top = Node(data, self.top)
        self.size += 1

    def pop(self):
        """Removes and returns the data from the top of the stack."""
        if self.isEmpty():
            raise KeyError("The stack is empty.")
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def peek(self):
        """Returns the data from the top of the stack without removing it."""
        if self.isEmpty():
            raise KeyError("The stack is empty.")
        return self.top.data


def main():
    """Tests the stack class."""
    s = Stack([1, 2, 3])
    print("Expect 3:", len(s))
    print("Expect [3, 2, 1]:", s)
    print("Expect 3:", s.peek())
    print("Expect 3:", s.pop())
    print("Expect 2:", len(s))
    print("Expect [2, 1]:", s)
    print("Expect 2:", s.peek())
    print("Expect 2:", s.pop())
    print("Expect 1:", s.peek())
    print("Expect 1:", s.pop())
    print("Expect True:", s.isEmpty())
    s.push(1)
    print("Expect 1:", s.peek())
    s.push(2)
    print("Expect 2:", s.peek())
    s.push(3)
    print("Expect 3:", s.peek())


if __name__ == "__main__":
    main()
