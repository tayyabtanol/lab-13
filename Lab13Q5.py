'''○ Implement functions to:■ Find the k-th smallest element in a BST'''

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def kth_smallest_bst(root, k):
    # Helper function to perform in-order traversal and keep track of visited nodes
    def in_order_traversal(node):
        if node is None:
            return []
        return in_order_traversal(node.left) + [node.value] + in_order_traversal(node.right)

    # Perform in-order traversal
    in_order_elements = in_order_traversal(root)

    # Check if k is within the valid range
    if 1 <= k <= len(in_order_elements):
        return in_order_elements[k - 1]
    else:
        return None

# Example usage:
# Create a sample binary search tree
#         3
#        / \
#       1   4
#        \
#         2
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)

# Find the 2nd smallest element in the BST
kth_element = kth_smallest_bst(root, 2)
print("2nd smallest element in the BST:", kth_element)
