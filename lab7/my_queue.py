"""
Author: Mohamed Soliman
File: my_queue.py
I changed the file name from queue.py to my_queue.py to avoid conflict with the built-in queue module.
"""

from node import Node


class Queue:
    """Represents a queue."""

    def __init__(self):
        """Creates an empty queue."""
        self.front = None
        self.rear = None
        self.size = 0

    def __len__(self):
        """Returns the number of items in the queue."""
        return self.size

    def __str__(self):
        """Returns the string representation of the queue."""
        return "[" + ", ".join(map(str, self)) + "]"

    def __iter__(self):
        """Supports iteration over a view of self."""
        # user should not need to iterate over the queue, but I added that to be able to use the __str__ in debugging
        cursor = self.front
        while cursor is not None:
            yield cursor.data
            cursor = cursor.next

    def __contains__(self, item):
        """Determines if the given item is in the queue."""
        for i in self:
            if i == item:
                return True
        return False

    def isEmpty(self):
        """Returns True if the queue is empty or False otherwise."""
        return self.front is None

    def push(self, item):
        """Adds the given item to the rear of the queue."""
        newNode = Node(item)
        if self.rear == None:
            self.rear = self.front = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
        self.size += 1

    def pop(self):
        """Removes and returns the data from the front of the queue."""
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        data = self.front.data
        if len(self) == 1:
            self.front = self.rear = None
        else:
            self.front = self.front.next

        self.size -= 1
        return data

    def peek(self):
        """Returns the item at the front of the queue."""
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        return self.front.data


def main():
    """Tests the queue class."""
    q = Queue()
    print("Queue is empty, expect True:", q.isEmpty())
    q.push(25)
    print("25 in queue, expect True:", 25 in q)
    print("24 in queue, expect False:", 24 in q)
    print("Peek at the front, expect 25:", q.peek())
    print("Pop 25, expect 25:", q.pop())
    print("Queue is empty, expect True:", q.isEmpty())
    for item in range(1, 11):
        q.push(item)
    print(q)
    for _ in range(5):
        print(q.pop())
    print(q)


if __name__ == "__main__":
    main()
