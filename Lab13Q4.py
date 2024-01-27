'''○ Implement functions to:■ Find the lowest common ancestor (LCA) of two nodes'''

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_lca(root, node1, node2):
    if root is None:
        return None

    # If either node1 or node2 is the root, then the root is the LCA
    if root.value == node1 or root.value == node2:
        return root

    # Recursively search for the LCA in the left and right subtrees
    left_lca = find_lca(root.left, node1, node2)
    right_lca = find_lca(root.right, node1, node2)

    # If both left and right LCA are not None, then the current root is the LCA
    if left_lca is not None and right_lca is not None:
        return root

    # If one of the subtrees has the LCA, return it; otherwise, return the other one
    return left_lca if left_lca is not None else right_lca

# Example usage:
# Create a sample binary tree
#         3
#        / \
#       5   1
#      / \ / \
#     6  2 0  8
#       / \
#      7   4
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

# Find the Lowest Common Ancestor (LCA) of nodes 5 and 1
lca_node = find_lca(root, 5, 1)
print("Lowest Common Ancestor of nodes 5 and 1:", lca_node.value)
