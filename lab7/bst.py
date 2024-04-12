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

    def preorder(self):
        """Returns a list of the items in the tree using a preorder traversal."""
        preorder_list = []

        def recurse(node):
            if node is not None:
                preorder_list.append(node.data)
                recurse(node.left)
                recurse(node.right)

        recurse(self.root)
        return preorder_list

    def inorder(self):
        """Returns a list of the items in the tree using an inorder traversal."""
        inorder_list = []

        def recurse(node):
            if node is not None:
                recurse(node.left)
                inorder_list.append(node.data)
                recurse(node.right)

        recurse(self.root)
        return inorder_list

    def postorder(self):
        """Returns a list of the items in the tree using an postorder traversal."""
        postorder_list = []

        def recurse(node):
            if node is not None:
                recurse(node.left)
                recurse(node.right)
                postorder_list.append(node.data)

        recurse(self.root)
        return postorder_list

    def balanced(self):
        "balances the tree."
        # I think clearing the tree and adding the items to it again would be easier than creating a new tree.
        items = self.inorder()
        self.root = None
        self._size = 0

        def recurse(left, right):
            if left <= right:
                middle = (left + right) // 2
                self.add(items[middle])
                recurse(left, middle - 1)
                recurse(middle + 1, right)

        recurse(0, len(items) - 1)


def main():
    """Main function for testing."""
    tree = BST(range(1, 8))
    tree.balanced()
    print("Should print a tree of nodes from 1 to 7:\n")
    print(tree)

    print("Should print items in preorder, inorder, and postorder:\n")
    print(tree.preorder())
    print(tree.inorder())
    print(tree.postorder())
    print()
    print()

    skinny_tree = BST(range(1, 8))
    print("Should print a skinny tree:\n")
    print(skinny_tree)
    skinny_tree.balanced()
    print("Should print the tree after being balanced:\n")
    print(skinny_tree)


if __name__ == "__main__":
    main()
