'''Implement functions to:
■ Calculate the height of a binary tree'''

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_height(root):
    if root is None:
        return 0
    else:
        left_height = tree_height(root.left)
        right_height = tree_height(root.right)

        # Return the height of the tree rooted at 'root'
        return 1 + max(left_height, right_height)

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

# Calculate and print the height of the binary tree
height = tree_height(root)
print("Height of the binary tree:", height)
