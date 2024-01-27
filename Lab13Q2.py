'''Implement functions to:■ Count the number of nodes in a binary tree'''

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_nodes(root):
    if root is None:
        return 0
    else:
        # Recursively count nodes in the left and right subtrees
        left_count = count_nodes(root.left)
        right_count = count_nodes(root.right)

        # Return the total count, which is 1 (current node) plus counts from left and right subtrees
        return 1 + left_count + right_count

# Example usage:
# Create a sample binary tree
#         1
#        / \
#       2   3
#      / \
#     4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Count and print the number of nodes in the binary tree
node_count = count_nodes(root)
print("Number of nodes in the binary tree:", node_count)
