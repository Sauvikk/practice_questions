# Given preorder and inorder traversal of a tree, construct the binary tree.
#
#  Note: You may assume that duplicates do not exist in the tree.
# Example :
#
# Input :
#         Preorder : [1, 2, 3]
#         Inorder  : [2, 1, 3]
#
# Return :
#             1
#            / \
#           2   3


from Level6.Trees.BinaryTree import BinaryTree, Node


class Solution:

    def __init__(self):
        self.pre_index = 0

    def search(self, arr, start, end, value):
        for i in range(start, end + 1):
            if arr[i] == value:
                return i

    def generate_tree(self, pre_order, in_order, start, end):
        if start > end:
            return None
        node = Node(pre_order[self.pre_index])
        self.pre_index += 1
        if start == end:
            return node
        index = self.search(in_order, start, end, node.val)
        node.left = self.generate_tree(pre_order, in_order, start, index - 1)
        node.right = self.generate_tree(pre_order, in_order, index + 1, end)
        return node

    def solution(self, pre_order, in_order):
        if pre_order is None or in_order is None:
            return None
        return self.generate_tree(pre_order, in_order, 0, len(in_order) - 1)


Solution.pre_index = 0

res = Solution().solution(['A', 'B', 'D', 'E', 'C', 'F'], ['D', 'B', 'E', 'A', 'F', 'C'])
BinaryTree().in_order(res)
