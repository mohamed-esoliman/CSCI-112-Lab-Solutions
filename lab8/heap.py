class Heap:
    """Represents a heap data structure."""

    def __init__(self, sourceCollection=None):
        """Constructs a heap with the items in the source collection, if it is present."""
        self.heap = []
        self.size = 0

        if sourceCollection is not None:
            for item in sourceCollection:
                self.push(item)

    def __str__(self):
        """Returns a string representation of the heap."""

        return str(self.heap)

    def __len__(self):
        """Returns the number of items in the heap."""
        return self.size

    def __contains__(self, target):
        """Returns True if the target is in the heap, or False otherwise."""
        return target in self.heap

    def push(self, item):
        """Adds the item to the heap."""
        self.heap.append(item)
        self.size += 1

        self.shiftUp(len(self.heap) - 1)

    def pop(self, index=0):
        """Removes and returns an item from the heap."""
        if self.size == 0:
            raise IndexError("cannot pop from an empty heap")

        self.size -= 1
        topItem = self.heap[0]
        bottomItem = self.heap.pop(len(self.heap) - 1)

        if self.size == 0:
            return topItem

        self.heap[index] = bottomItem
        self.shiftDown(index)
        return topItem

    def shiftUp(self, curPos):
        """Moves the item at the given index up to its proper position."""

        while curPos > 0:
            parentPos = (curPos - 1) // 2

            item = self.heap[curPos]
            parent = self.heap[parentPos]

            if parent <= item:
                break
            else:
                self.swap(curPos, parentPos)
                curPos = parentPos

    def shiftDown(self, curPos):
        """Moves the item at the given index down to its proper position."""

        maxIndex = len(self.heap) - 1

        while True:
            leftChildIndex = curPos * 2 + 1
            rightChildIndex = curPos * 2 + 2

            if leftChildIndex > maxIndex:
                break
            elif rightChildIndex > maxIndex:
                minChildIndex = leftChildIndex
            else:
                leftChild = self.heap[leftChildIndex]
                rightChild = self.heap[rightChildIndex]

                if leftChild <= rightChild:
                    minChildIndex = leftChildIndex
                else:
                    minChildIndex = rightChildIndex

            minChild = self.heap[minChildIndex]

            if self.heap[curPos] <= minChild:
                break
            else:
                self.swap(curPos, minChildIndex)
                curPos = minChildIndex

    def swap(self, i, j):
        """Swaps the items at the given indices."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


def main():
    """Tests the heap class."""
    h = Heap([10, 5, 20, 3, 8, 15, 25, 7, 12, 37, 26, 2, 17])
    print(
        "Constructed a heap with unordered numbers. Should print a list representation of the heap:"
    )
    print(h)
    print(
        "The length of the heap is (should be 13):",
    )
    print(len(h))
    print("25 in the heap, expect True:", 25 in h)
    print("24 in the heap, expect False:", 24 in h)
    print("Popping the topmost item (should be 2):")
    print(h.pop())
    print("Should print a list representation of the heap after popping 2:")
    print(h)
    h.push(1)
    print(
        "Pushed 1 to the heap. Should print a list representation of the heap after pushing 1:"
    )
    print(h)


if __name__ == "__main__":
    main()
