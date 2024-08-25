from math import log2, ceil
import random
from my_queue import Queue
from time import time


class Node:
    """Represents a node in a binary tree."""

    def __init__(self, data, left=None, right=None):
        """Initializes the node with the given data and children."""
        self.data = data
        self.left = left
        self.right = right
        self.depth = None


class BT:
    """Represents a general binary tree."""

    def __init__(self, sourceCollection=None):
        """Initializes the tree with a root node and sets the size to 0. If a source collection is given, the tree is initialized with the items in the collection."""
        self.root = None
        self._size = 0

        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def __str__(self):
        """Returns a string representation with the tree rotated 90 degrees counterclockwise."""

        def recurse(node, level):
            treeStr = ""
            if node is not None:
                treeStr += recurse(node.right, level + 1)
                treeStr += "   " * level + str(node.data) + "\n"
                treeStr += recurse(node.left, level + 1)
            return treeStr

        return recurse(self.root, 0)

    def __len__(self):
        """Returns the number of items in the tree."""
        return self._size

    # def __contains__(self, target):
    #     """Returns True if the item is in the tree, or False otherwise."""

    #     def recurse(node):
    #         if node is None:
    #             return False
    #         elif node.data == target:
    #             return True
    #         elif node.data > target:
    #             return recurse(node.left)
    #         elif node.data < target:
    #             return recurse(node.right)

    #     return recurse(self.root)

    def bfs(self, target, depth_limit=None, verbose=False):

        def successors(node):
            children = []
            if node.left is not None:
                children.append(node.left)
            if node.right is not None:
                children.append(node.right)
            return children

        if self.root is None:
            raise Exception("cannot search an empty tree!")

        bfs_q = Queue()
        bfs_q.push(self.root)

        while not bfs_q.isEmpty():
            current = bfs_q.pop()
            if depth_limit is not None:
                if current.depth > depth_limit:
                    print(f"Maxed out at depth {depth_limit}; quitting...")
                    break

            if verbose:
                print(str(current.data) + "  at depth: " + str(current.depth))

            if current.data == target:
                return True
            else:
                for item in successors(current):
                    bfs_q.push(item)
        return False

    def isEmpty(self):
        """Returns True if the tree is empty, or False otherwise."""
        return self._size == 0

    def add(self, item):
        """Adds the item to the tree in its proper location."""

        NewNode = Node(item)

        if self.root is None:
            self.root = NewNode
        else:
            q = Queue()
            q.push(self.root)

            while not q.isEmpty():
                node = q.pop()

                if node.left is None and node.right is None:
                    if random.random() <= 0.5:
                        node.left = NewNode
                        break
                    else:
                        node.right = NewNode
                        break

                if node.left is None:
                    node.left = NewNode
                    break
                else:
                    q.push(node.left)

                if node.right is None:
                    node.right = NewNode
                    break
                else:
                    q.push(node.right)

        self._size += 1
        NewNode.depth = self.height() + 1

    def height(self):
        """Returns the height of the tree"""
        return ceil(log2(len(self) + 1)) - 1


def main():
    """Main function for testing."""
    tree = BT(range(1, 26))
    print("Added the range 1 - 26 to a BT tree. Should print a balanced tree:\n")
    print(tree)

    print(
        "Testing the bfs search method. 23 is in the tree. Should print the nodes it visits and then true:"
    )
    print(tree.bfs(23, verbose=True))
    print()
    print("27 is not in the tree. Should print false:")
    print(tree.bfs(27))
    print()
    print()

    print("Building a tree with 2000 nodes. Could take a few seconds...")
    big_tree = BT(range(2000))
    print(f"Tree has a height of {big_tree.height()}")
    print()

    print("FULL BFS for target 10000:")
    start = time()
    print(big_tree.bfs(10000))
    print(round(time() - start, 5) * 1000, "milli seconds.")
    print()
    print()

    print("FULL BFS for a missing datum:")
    start = time()
    print(big_tree.bfs(20000))
    print(round(time() - start, 5) * 1000, "milli seconds.")
    print()
    print()

    print("BFS for a missing datum; depth limited to 10:")
    start = time()
    print(big_tree.bfs(20000, depth_limit=10))
    print(round(time() - start, 5) * 1000, "milli seconds.")
    print()
    print()


if __name__ == "__main__":
    main()
