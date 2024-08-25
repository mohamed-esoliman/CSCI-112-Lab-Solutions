"""
Author: Mohamed Soliman
File: my_priorityQueue2.py
"""

from heap import Heap


class PriorityQueue:
    """Represents a priority queue."""

    def __init__(self, sourceCollection=None):
        """Creates an empty queue."""
        self.heap = Heap(sourceCollection)

    def __len__(self):
        """Returns the number of items in the queue."""
        return len(self.heap)

    def __str__(self):
        """Returns the string representation of the heap used in this queue."""
        return str(self.heap)

    def __contains__(self, item):
        """Determines if the given item is in the queue."""
        return item in self.heap

    def push(self, item):
        """
        Adds the given item to the rear of the queue with priority based on the item's value.
        The smaller the value, the higher the priority. When two elements have the same priority,
        they are served in FIFO order

        """
        self.heap.push(item)

    def pop(self):
        """Removes and returns the data from the front of the queue."""
        return self.heap.pop()


def main():
    """Tests the priority queue class."""
    pq = PriorityQueue([13, 25, 5, 3, 100, 11, 30, 17, 45, 9])
    print(
        "Constructed a priority queue with unordered items. Should print the heap representation of the priority queue:"
    )
    print(pq)
    print("Pop the topmost item, expect 3:", pq.pop())
    print(
        "Should print the heap representation of the priority queue after popping the topmost item:"
    )
    print(pq)
    print("Pop the first 3 items:")
    for _ in range(3):
        print(pq.pop())
    print(
        "Should print the heap representation of the priority queue after popping the first 3 items:"
    )
    print(pq)


if __name__ == "__main__":
    main()
