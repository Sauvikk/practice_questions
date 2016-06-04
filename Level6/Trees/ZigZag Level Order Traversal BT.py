# Given a binary tree, return the zigzag level order traversal of
# its nodes’ values. (ie, from left to right, then right to left for the next level and alternate between).
#
# Example :
# Given binary tree
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return
#
# [
#          [3],
#          [20, 9],
#          [15, 7]
# ]
# http://articles.leetcode.com/printing-binary-tree-in-zig-zag-level_18/


from Level6.Trees.BinaryTree import BinaryTree, Node
# from collections import deque


class Solution:

    def solution(self, root):
        if not root:
            return
        current_level = []
        next_level = []
        current_level.append(root)
        left_to_right = True
        temp = []
        result = []
        while len(current_level) > 0:
            curr_node = current_level[-1]
            current_level.pop()
            if curr_node:
                temp.append(curr_node.val)
                if left_to_right:
                    next_level.append(curr_node.left)
                    next_level.append(curr_node.right)
                else:
                    next_level.append(curr_node.right)
                    next_level.append(curr_node.left)
            if len(current_level) == 0:
                if temp:
                    result.append(temp)
                temp = []
                left_to_right = not left_to_right
                current_level, next_level = next_level, current_level
        return result

node = Node(3)
node.left = Node(9)
node.right = Node(20)
node.right.left = Node(15)
node.right.right = Node(7)
res = Solution().solution(node)
print(res)
