from math import log2, ceil


class Node:
    """Represents a node in a binary tree."""

    def __init__(self, data, left=None, right=None):
        """Initializes the node with the given data and children."""
        self.data = data
        self.left = left
        self.right = right


class BST:
    """Represents a binary search tree."""

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

    def __contains__(self, target):
        """Returns True if the item is in the tree, or False otherwise."""

        def recurse(node):
            if node is None:
                return False
            elif node.data == target:
                return True
            elif node.data > target:
                return recurse(node.left)
            elif node.data < target:
                return recurse(node.right)

        return recurse(self.root)

    def isEmpty(self):
        """Returns True if the tree is empty, or False otherwise."""
        return self._size == 0

    def add(self, item):
        """Adds the item to the tree in its proper location."""

        NewNode = Node(item)

        def recurse(node):
            if item < node.data:
                if node.left is None:
                    node.left = NewNode
                else:
                    recurse(node.left)
            else:
                if node.right is None:
                    node.right = NewNode
                else:
                    recurse(node.right)

        if self.isEmpty():
            self.root = NewNode
        else:
            recurse(self.root)

        self._size += 1

    def height(self):
        """Returns the height of the tree. The height is the number of steps to the deepest levels."""

        def recurse(node):
            if node is None:
                return 0
            else:
                branchesDepth = [recurse(node.left), recurse(node.right)]
                return 1 + max(branchesDepth)

        return (
            recurse(self.root) - 1
        )  # Subtract 1 to get the number of steps, not levels

    def isBalanced(self):
        """Returns True if the tree is balanced, or False otherwise."""
        return self.height() < ceil(log2(len(self)))


def main():
    """Main function for testing."""
    tree = BST()
    tree.add(5)
    tree.add(3)
    tree.add(8)
    print("Should print a tree with 5, 3, 8 added:\n")
    print(tree)

    print("The tree contains 3. Should be true:", (3 in tree))
    print("The tree contains 10. Should be false:", (10 in tree))
    print("Should print the length of the tree:", len(tree))
    print("Is the tree empty? Should be false:", tree.isEmpty())
    tree.add(10)
    print("Should print the tree after adding 10:\n", tree)
    print("Should print the new length of the tree:", len(tree))
    print("Should print the height of the tree:", tree.height())

    print(
        "\n\n\n\n-----------------------------\nBalance Test\n-----------------------------\n"
    )

    skinnyTree = BST()
    skinnyTree.add(1)
    skinnyTree.add(2)
    skinnyTree.add(3)
    skinnyTree.add(4)
    print("Should print a skinny tree:\n")
    print(skinnyTree)

    balancedTree = BST()
    balancedTree.add(5)
    balancedTree.add(3)
    balancedTree.add(9)
    balancedTree.add(1)
    balancedTree.add(4)
    balancedTree.add(8)
    balancedTree.add(10)
    print("Should print a balanced tree:\n")
    print(balancedTree)

    print("Is the skinny tree balanced? Should be false:", skinnyTree.isBalanced())
    print("Is the balanced tree balanced? Should be true:", balancedTree.isBalanced())


if __name__ == "__main__":
    main()
