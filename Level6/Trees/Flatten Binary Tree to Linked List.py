# Given a binary tree, flatten it to a linked list in-place.
#
# Example :
# Given
#
#
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6
# Note that the left child of all nodes should be NULL.


from Level6.Trees.BinaryTree import BinaryTree, Node


class Solution:
    def sol(self, root):
        root1 = root
        while root:
            if root.left is None:
                root = root.right
            else:
                tmp = root.left
                while tmp.right:
                    tmp = tmp.right
                tmp.right = root.right
                root.right = root.left
                root.left = None
        return root1



