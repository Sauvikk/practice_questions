# Given a binary tree and a sum, find all root-to-leaf paths where each path’s sum equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]


from Level6.Trees.BinaryTree import BinaryTree, Node


class Solution:

    def generate_path(self, root, target, result, temp):
        if root.left is None and root.right is None and target == 0:
            result.append(temp[:])

        if root.left:
            temp.append(root.left.val)
            self.generate_path(root.left, target-root.left.val, result, temp)
            temp.pop()

        if root.right:
            temp.append(root.right.val)
            self.generate_path(root.right, target-root.right.val, result, temp)
            temp.pop()

    def solution(self, root, target):
        result = []
        if root is None:
            return result
        temp = [root.val]
        self.generate_path(root, target-root.val, result, temp)
        return result


root = Node(5)
root.left = Node(4)
root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(2)
root.right = Node(8)
root.right.right = Node(4)
root.right.left = Node(13)
root.right.right.right = Node(1)
root.right.right.left = Node(5)
res = Solution().solution(root, 22)
print(res)
