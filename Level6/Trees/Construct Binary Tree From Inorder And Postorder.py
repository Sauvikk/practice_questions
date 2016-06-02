# Given inorder and postorder traversal of a tree, construct the binary tree.
#
#  Note: You may assume that duplicates do not exist in the tree.
# Example :
#
# Input :
#         Inorder : [2, 1, 3]
#         Postorder : [2, 3, 1]
#
# Return :
#             1
#            / \
#           2   3


from Level6.Trees.BinaryTree import BinaryTree, Node


class Solution:

    def __init__(self):
        self.post_index = 0

    def assign(self, val):
        self.post_index = val

    def search(self, arr, start, end, value):
        for i in range(start, end + 1):
            if arr[i] == value:
                return i

    def generate_tree(self, post_order, in_order, start, end):
        if start > end:
            return None
        node = Node(post_order[self.post_index])
        self.post_index -= 1
        if start == end:
            return node
        index = self.search(in_order, start, end, node.val)
        node.right = self.generate_tree(post_order, in_order, index + 1, end)
        node.left = self.generate_tree(post_order, in_order, start, index - 1)
        return node

    def solution(self, post_order, in_order):
        if post_order is None or in_order is None:
            return None
        self.assign(len(in_order)-1)
        return self.generate_tree(post_order, in_order, 0, len(in_order) - 1)


in_o = [4, 8, 2, 5, 1, 6, 3, 7]
post = [8, 4, 5, 2, 6, 7, 3, 1]
res = Solution().solution(post, in_o)
BinaryTree().pre_order(res)
