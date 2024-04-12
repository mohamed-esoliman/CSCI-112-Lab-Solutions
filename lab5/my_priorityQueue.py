"""
Author: Mohamed Soliman
File: my_priorityQueue.py
"""

from node import Node


class PriorityQueue:
    """Represents a priority queue."""

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
        """
        Adds the given item to the rear of the queue with priority based on the item's value.
        The smaller the value, the higher the priority. When two elements have the same priority,
        they are served in FIFO order

        """
        newNode = Node(item)
        if self.rear == None:
            self.rear = self.front = newNode

            self.size += 1
            return 0
        else:
            if newNode.data < self.front.data:
                newNode.next = self.front
                self.front = newNode

                self.size += 1
                return 0
            elif newNode.data > self.rear.data:
                self.rear.next = newNode
                self.rear = newNode

                self.size += 1
                return len(self) - 1
            else:
                current = self.front
                i = 1
                while current.next is not None and current.next.data <= newNode.data:
                    current = current.next
                    i += 1
                newNode.next = current.next
                current.next = newNode

                self.size += 1
                return i

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
    """Tests the priority queue class."""
    pq = PriorityQueue()
    print("Queue is empty, expect True:", pq.isEmpty())
    print(pq.push(25))
    print(pq.push(22))
    print(pq.push(23))
    print(pq.push(27))
    print(pq.push(26))
    print(pq)
    print("25 in queue, expect True:", 25 in pq)
    print("24 in queue, expect False:", 24 in pq)
    print("Peek at the front, expect 22:", pq.peek())
    print("Pop 22, expect 22:", pq.pop())
    for _ in range(4):
        print(pq.pop())
    print("Queue is empty, expect True:", pq.isEmpty())
    for item in [13, 27, 5, 3, 100, 11, 30, 17, 45, 9, 5, 3, 100, 11, 30, 17, 45, 9]:
        pq.push(item)
    print(pq)
    for _ in range(5):
        print(pq.pop())
    print(pq)
    pq_chars = PriorityQueue()
    for item in ["c", "a", "d", "b", "f", "e"]:
        pq_chars.push(item)
    print(pq_chars)


if __name__ == "__main__":
    main()
