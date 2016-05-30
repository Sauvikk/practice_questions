# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
#
#  Balanced tree : a height-balanced binary tree is defined as a
#  binary tree in which the depth of the two subtrees of every node never differ by more than 1.
# Example :
#
#
# Given A : [1, 2, 3]
# A height balanced BST  :
#
#       2
#     /   \
#    1     3


from Level6.Trees.BinaryTree import BinaryTree, Node


class Solution:

    def generate_bt(self, num, start, end):
        if start > end:
            return None
        mid = int((start+end)/2)
        node = Node(num[mid])
        node.left = self.generate_bt(num, start, mid-1)
        node.right = self.generate_bt(num, mid+1, end)
        return node

    def solution(self, num):
        if num is None or len(num) == 0:
            return num
        return self.generate_bt(num, 0, len(num)-1)


res = Solution().solution([1, 2, 3, 4, 5, 6, 7])
BinaryTree().pre_order(res)
