"""
Author: Mohamed Soliman
File: arraysortedbag.py
"""

from arrays import Array


class ArraySortedBag(object):
    """An array-based bag implementation."""

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._items = Array(ArraySortedBag.DEFAULT_CAPACITY)
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return len(self) == 0

    def __len__(self):
        """Returns the number of items in self."""
        return self._size

    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = ArraySortedBag(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other:
            return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        for item in self:
            if not item in other or not self.count(item) == other.count(item):
                return False
        return True
        # problem: returns false when applied on a clone

    def __contains__(self, item):
        """Uses binary search to check membership"""
        left = 0
        right = self._size - 1

        while left <= right:
            midpoint = (left + right) // 2
            if item == self._items[midpoint]:
                return True
            elif item < self._items[midpoint]:
                right = midpoint - 1
            else:
                left = midpoint + 1
        return False

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = Array(ArraySortedBag.DEFAULT_CAPACITY)

    def add(self, item):
        """Adds item to self in the appropriate position."""
        # Check array memory here and increase it if necessary
        if self._size == len(self._items):
            temp = Array(2 * len(self))
            for i in range(self._size):
                temp[i] = self._items[i]
            self._items = temp

        insertIndex = 0

        for i in range(self._size):
            if self._items[i] > item:
                insertIndex = i
                break
            else:
                insertIndex = self._size

        for j in range(self._size, insertIndex, -1):
            self._items[j] = self._items[j - 1]

        self._items[insertIndex] = item
        self._size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        # Check precondition and raise exception if necessary
        if not item in self:
            raise KeyError(str(item) + " not in bag")
        # Search for the index of the target item
        targetIndex = 0
        for targetItem in self:
            if targetItem == item:
                break
            targetIndex += 1
        # Shift items to the left of target up by one position
        for i in range(targetIndex, len(self) - 1):
            self._items[i] = self._items[i + 1]
        # Decrement logical size
        self._size -= 1
        # Check array memory here and decrease it if necessary
        if (
            len(self._items) >= 2 * ArraySortedBag.DEFAULT_CAPACITY
            and self._size < len(self._items) // 4
        ):
            temp = Array(len(self._items) // 2)
            for i in range(self._size):
                temp[i] = self._items[i]
            self._items = temp

    def count(self, item):
        """Returns the number of occurences of items in self."""
        count = 0
        for i in range(self._size):
            if self._items[i] == item:
                count += 1
        return count
