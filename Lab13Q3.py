'''○ Implement functions to:■ Determine if a tree is a BST'''

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True

    # Check if the current node's value is within the valid range
    if not (min_val < root.value < max_val):
        return False

    # Recursively check the left and right subtrees
    return (is_bst(root.left, min_val, root.value) and
            is_bst(root.right, root.value, max_val))

# Example usage:
# Create a sample binary search tree
#         2
#        / \
#       1   3
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

# Check if the binary tree is a BST
result = is_bst(root)
print("Is the binary tree a BST?", result)
