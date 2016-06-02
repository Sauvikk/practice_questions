# Given an inorder traversal of a cartesian tree, construct the tree.
#
#  Cartesian tree : is a heap ordered binary tree, where the root is greater than all the elements in the subtree.
#  Note: You may assume that duplicates do not exist in the tree.
# Example :
#
# Input : [1 2 3]
#
# Return :
#           3
#          /
#         2
#        /
#       1


from Level6.Trees.BinaryTree import BinaryTree, Node


class Solution:

    def max_array(self, arr, start, end):
        maximum = arr[start]
        max_index = start
        for i in range(start+1, end+1):
            if arr[i] > maximum:
                maximum = arr[i]
                max_index = i
        return max_index

    def generate_tree(self, arr, start, end):
        if start > end:
            return None
        index = self.max_array(arr, start, end)
        node = Node(arr[index])
        if start == end:
            return node
        node.left = self.generate_tree(arr, start, index-1)
        node.right = self.generate_tree(arr, index+1, end)
        return node

    def solution(self, arr):
        if arr is None:
            return 0
        return self.generate_tree(arr, 0, len(arr)-1)


res = Solution().solution([5, 10, 40, 30, 28, 1, 2, 3])
BinaryTree().in_order(res)
