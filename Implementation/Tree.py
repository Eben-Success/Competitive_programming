class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self) :
        self.root = None


    
    def insert_node(self, val):
        """
        In average case, the time is O(logn): tree is balanced
        Time in worst case is O(n): height of the BST
        """
        new_node = Node(val)

        if self.root is None:
            self.root = new_node

        current = self.root

        if val < current.val:
            if current.left is None:
                current.left = new_node
                return 
            # traverses the left of the tree.
            current = current.left

        else:
            if current.right is None:
                current.right = new_node
                return 
            # traverse the right of the tree
            current = current.right

    def get_node(self, root, val):
        """Average time: O(logn) when tree is balanced.
        Worst case: O(n): height of the BST"""

        if root is None or root.val == val:
            return root

        if val < root.val:
            return self.get_node(root.left, val)
        else:
            return self.get_node(root.right, val)

    # Iterative Approach
    # Return boolean if node if found
    def search(self, root, key):
        while root is not None:
            if key == root:
                return True
            elif key < root:
                root = root.left
            else:
                root = root.right
        return False

    # Recursive Approach
    def search_recursive(self, root, key):
        if root is None or root.val == key:
            return root is not None
        elif key < root.val:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    # delete a node from the BST
    def delete_node(self, val):
        """
        Base case: if the node is empty.
        Edge cases:
        1. The node has on child
        2. The node has one child
        3. The node has two children.
        """

        self.root = self._delete_node(self.root, val)

    
    # private method to delete node
    def _delete_node(self, node, val):
        if not node:
            return None

        if val < node.val:
            node.left = self._delete_node(node.left, val)
        elif val > node.val:
            node.right = self._delete_node(node.right, val)

        else:
            # if node has no child

            if not node.left and not node.right:
                return None

            # if node has one child
            elif not node.left:
                return node.right

            elif not node.right:
                return node.left

            else:
                # the node has 2 children
                """
                In-order successor is used when deleting a node with 2 children.
                In an in-order traversal, the nodes are visited in increasing order, 
                so the in-order successor is the next node that would be visited 
                in the traversal.
                By replacing the node to be deleted with its in-order successor, 
                we ensure that the ordering property of BST is maintained.
                """

                in_order_successor = self._find_min(node.right)
                node_val = in_order_successor.val
                node.right = self._delete_node(node.right, in_order_successor)

        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node


        






        