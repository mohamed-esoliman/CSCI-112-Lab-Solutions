"""
Implementations of dictionaries using different data structures.
Author: Mohamed Soliman
"""

from bst import BST
from time import time
import string


class Entry:
    """A key-value pair."""

    def __init__(self, key, value):
        """Initializes the entry with the given key and value."""
        self.key = key
        self.value = value
        self.next = None

    def __eq__(self, other):
        """Returns True if the keys are equal, or False otherwise."""
        return self.key == other.key

    def __lt__(self, other):
        """Returns True if the key is less than the other's key, or False otherwise."""
        return self.key < other.key

    def __gt__(self, other):
        """Returns True if the key is greater than the other's key, or False otherwise."""
        return self.key > other.key

    def __str__(self):
        """Returns a string representation of the entry."""
        return str(self.key) + ": " + str(self.value)


class BstDictionary:
    """A dictionary implemented using a binary search tree."""

    def __init__(self):
        """Initializes an empty dictionary."""
        self.bst = BST()

    def __setitem__(self, key, value):
        """Inserts a new entry with the given key and value."""
        newEntry = Entry(key, value)

        if not newEntry in self.bst:
            self.bst.add(newEntry)
        else:
            self.bst.find(newEntry).value = value

    def __getitem__(self, key, defaultValue=None):
        """Returns the value associated with the given key."""
        keyEntry = Entry(key, None)
        wantedEntry = self.bst.find(keyEntry)
        return wantedEntry.value if wantedEntry is not None else defaultValue

    def __contains__(self, key):
        """Returns True if the key is in the dictionary, or False otherwise."""
        return Entry(key, None) in self.bst

    def __iter__(self):
        """Supports iteration over a view of self."""
        return self.bst.__iter__()

    def __str__(self):
        """Returns a string representation of the dictionary."""
        allItems = []
        for entry in self.bst:
            allItems.append(str(entry))
        dictStr = "{" + ", ".join(allItems) + "}"
        return dictStr

    def __len__(self):
        """Returns the number of items in the dictionary."""
        return len(self.bst)


class HashDictionary:
    """A dictionary implemented using a hash table."""

    DEFAULT_CAPACITY = 1000

    def __init__(self, capacity=DEFAULT_CAPACITY):
        """Initializes an empty dictionary."""
        self.array = [None] * capacity
        self.size = 0

    def __hash(self, key):
        """Returns the hash value of the key."""
        return abs(hash(key)) % len(self.array)

    def __setitem__(self, key, value):
        """Inserts a new entry with the given key and value."""
        SearchIndex = self.__hash(key)
        if key in self:
            cursor = self.array[SearchIndex]
            while cursor.key != key:
                cursor = cursor.next
            cursor.value = value
            return True
        else:
            NewEntry = Entry(key, value)
            NewEntry.next = self.array[SearchIndex]
            self.array[SearchIndex] = NewEntry
            self.size += 1
            return True

    def __getitem__(self, key, defaultValue=None):
        """Returns the value associated with the given key."""
        SearchIndex = self.__hash(key)
        cursor = self.array[SearchIndex]
        while cursor is not None:
            if cursor.key == key:
                return cursor.value
            cursor = cursor.next
        return defaultValue

    def remove(self, key):
        """removes an entry from the dictionary using its key."""
        if key not in self:
            return False
        else:
            searchIndex = self.__hash(key)
            cursor = self.array[searchIndex]
            if cursor.key == key:
                self.array[searchIndex] = cursor.next
                self.size -= 1
                return
            while not cursor.next.key == key:
                cursor = cursor.next
            cursor.next = cursor.next.next
            self.size -= 1
            return

    def __contains__(self, key):
        """Returns True if the key is in the dictionary, or False otherwise."""
        searchIndex = self.__hash(key)
        cursor = self.array[searchIndex]
        while cursor is not None:
            if cursor.key == key:
                return True
            cursor = cursor.next
        return False

    def __iter__(self):
        """Supports iteration over a view of self."""
        for item in self.array:
            cursor = item
            while cursor is not None:
                yield cursor
                cursor = cursor.next

    def __str__(self):
        """Returns a string representation of the dictionary."""
        allItems = []
        for item in self:
            allItems.append(str(item))
        dictStr = "{" + ", ".join(allItems) + "}"
        return dictStr

    def __len__(self):
        """Returns the number of items in the dictionary."""
        return self.size


def main():
    """Main function to test the dictionary implementations."""
    print("Part I: BST Dictionary ------------")
    print()
    d1 = BstDictionary()
    d1["b"] = 2
    d1["d"] = 4
    d1["a"] = 1
    d1["c"] = 3
    # d["e"] = 5
    d1["f"] = 6
    d1["g"] = 7

    print(
        "added a, b, c, d, f, g to the dictionary. Should print the dictionary in order."
    )
    print(d1)
    print()

    d1["a"] = 4
    print("changed the value of a to 4. Should print the dictionary in order.")
    print(d1)
    print()

    print("Should print the length of the dictionary (should be 6):")
    print(len(d1))
    print()

    print("Should print the value of b (should be 2):")
    print(d1["b"])
    print("Should print the value of a (should be 4):")
    print(d1["a"])
    print("Should print the value of e (should be None):")
    print(d1["e"])
    print()

    print("Searching a in the dictionary. Should be True:")
    print("a" in d1)
    print("Searching b in the dictionary. Should be True:")
    print("b" in d1)
    print("Searching u in the dictionary. Should be False:")
    print("u" in d1)
    print()

    print("Should print the dictionary in order:")
    for key in d1:
        print(key)

    print("*" * 50)
    print("\n\n")

    print("Part II: Hash Dictionary ------------")
    print()

    d2 = HashDictionary()
    d2["b"] = 2
    d2["d"] = 4
    d2["a"] = 1
    d2["c"] = 3
    # d2["e"] = 5
    d2["f"] = 6
    d2["g"] = 7

    print("added a, b, c, d, f, g to the dictionary. Should print the dictionary.")
    print(d2)
    print()

    d2["a"] = 4
    print("changed the value of a to 4. Should print the dictionary.")
    print(d2)
    print()

    print("Should print the length of the dictionary (should be 6):")
    print(len(d2))
    print()

    print("Should print the value of b (should be 2):")
    print(d2["b"])
    print("Should print the value of a (should be 4):")
    print(d2["a"])
    print("Should print the value of e (should be None):")
    print(d2["e"])
    print()

    print("Searching a in the dictionary. Should be True:")
    print("a" in d2)
    print("Searching b in the dictionary. Should be True:")
    print("b" in d2)
    print("Searching u in the dictionary. Should be False:")
    print("u" in d2)
    print()

    print("Should print the dictionary:")
    for key in d2:
        print(key)
    print()

    print("Removing a from the dictionary. Should print the dictionary:")
    d2.remove("a")
    print(d2)

    print()
    print()

    print(
        "Testing collision handling. Adding letters from a to h to a hash dictionary with a capacity of only 5."
    )
    d3 = HashDictionary(5)
    d3["a"] = 1
    d3["b"] = 2
    d3["c"] = 3
    d3["d"] = 4
    d3["e"] = 5
    d3["f"] = 6
    d3["g"] = 7
    d3["h"] = 8

    print("Should print the dictionary:")
    print(d3)

    print("*" * 50)
    print("\n\n")

    print("Part III: Moby Dictionaries ------------")

    print("Making word counts. This may take a while...")
    with open("mobydick.txt") as file:
        words = file.read().split()

    words = [s.translate(str.maketrans("", "", string.punctuation)) for s in words]
    vocabulary = set(words)
    vocabCount = [words.count(vocab) for vocab in vocabulary]

    bstDict = BstDictionary()
    hashDict = HashDictionary()
    print()
    print()

    print("Adding words to a BST dictionary")
    start = time()
    for word, count in zip(vocabulary, vocabCount):
        bstDict[word] = count
    timeBST = time() - start
    print(f"It took {round(timeBST, 5)} seconds add words to the BST dictionary.")
    print()
    print()

    print("Adding words to a hash dictionary")
    start = time()
    for word, count in zip(vocabulary, vocabCount):
        hashDict[word] = count
    timeHash = time() - start
    print(f"It took {round(timeHash, 5)} seconds add words to the hash dictionary.")


if __name__ == "__main__":
    main()
