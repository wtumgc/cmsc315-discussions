"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.

        # Save the value of this new node.
        self.value = value

        # Save a null value for the adjacent nodes.
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.

        # Create a tree which will be empty.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method. X
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node. X
        """

        # Save a value into the provided Binary Search Tree.
        #   Predicessor values (smaller) should be left adjecent.
        #   Successor values (larger) should be on the right.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found. X
        - Insert smaller values into the left subtree. X
        - Insert larger values into the right subtree. X
        - Return the updated node reference. X
        """

        # If the child node is empty, create a new node.
        if node is None:
            return Node(value)

        # If the new node value is smaller than the current node, update value to the left adjacent node.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # If the new node value is larger than the current node, update value to the right adjacent node.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Return the node to the last recursive call.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # This is just wrapper code, use the
        #   recursive search to traverse the tree.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """

        # If to bottom is reached and empty, then
        #   the value was not found and return 'false'.
        if node is None:
            return False

        # If the current node contains equals the provided value,
        #   the node was found so return 'true'.
        if value == node.value:
            return True

        # If the value provided is smaller than the current
        #   node value, search to the left.
        if value < node.value:
            return self._search_recursive(node.left, value)

        # If the value provided is larger than the current
        #   node value, search to the right.
        if value > node.value:
            return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """

        values = []

        # Use the recursive helper to perform the traversal.

        # This is just wrapper code, use the
        #   recursive inorder to traverse the tree.
        self._inorder_recursive(self.root, values)

        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """

        # If the bottom of the tree is reached, return.
        if node is None:
            return

        # Go to the left in the tree first.
        self._inorder_recursive(node.left, values)

        # Go to the current node.
        values.append(node.value)

        # Next, go to the right part of the tree.
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object. X
    # 2. Insert at least 7 values. X
    # 3. Include values that go into both left X
    #    and right subtrees. X
    # 4. Display the values inserted. X
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step. X

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    #   Create a binary search tree object
    binary_search_tree1 = BST()

    #   Create list of 7 values and update the new binary
    #       search tree with these values. Make them out
    #       of order to show how tree traversing works
    v = [55, 33, 99, 22, 77, 88, 44]
    for values in v:
        binary_search_tree1.insert(values)
    #   A binary search tree can be more efficient that a linear search. This is because
    #       much of the "tree" nodes can be eliminated by traversing to the left
    #       or right within the tree structure thereby bypassing nodes which would
    #       using computer cycles with a standard list based search.

    print("    Create list of values and inserted into new BST. The values are", v)


    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal. X
    # 2. Display the traversal results. X
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST. X

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    # Perform an in-order traversal of the BST.
    in_order_nodes = binary_search_tree1.inorder()

    # Display the traversal results. The traversal first moves to the leftmost
    #   part of the tree then traverses back up to the root then to the right.
    print("    Nodes using the 'inorder' method:", in_order_nodes)



# ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist. X
    # 2. Search for at least two values that do not exist. X
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")

    # The following node values EXIST and should return a value of 'true'.
    print("The following node values EXIST and should return a value of 'true'...")
    print("    Searching for 33:", binary_search_tree1.search(33))
    print("    Searching for 88:", binary_search_tree1.search(88))

    # The following node values DO NOT EXIST and should return a value of 'false'.
    print("# The following node values DO NOT EXIST and should return a value of 'false'...")
    print("    Searching for 40:", binary_search_tree1.search(40))
    print("    Searching for 100:", binary_search_tree1.search(100))

    #   The above results use a traversal also but to search. During the traversal of the
    #       BST, node value that exist should return a true value while those that do not
    #       exist should return a false value.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree X
    # - Search an empty tree X
    # - Insert duplicate values X
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")

    print("    Creating an empty BST named etree for edge case testing...")
    etree = BST()
    #   Created an empty BST named etree for edge case testing...")

    #   Search and traverse the empty BST. The result should be "False" for the
    #       and Null for the traversal.
    print("    Searching an empty tree:", etree.search(67))
    print("    Traverse an empty tree:", etree.inorder())

    #   Attempt to insert duplicate values.
    print("    Insert two of the same i.e., duplicate values in the empty tree "
          "along with other unique out of order values.")
    etree.insert(99)
    etree.insert(67)
    etree.insert(67)
    etree.insert(11)
    print("    Inserted value of 67 twice. The list traversal results are: ", etree.inorder())

    print("    Creating a BST named tree_1node for edge case testing with only 1 node...")
    tree_1node = BST()
    tree_1node.insert(69)
    print("    Inserted value of 69 so BST has only 1 node. The list traversal results are: ", tree_1node.inorder())


if __name__ == "__main__":
    main()