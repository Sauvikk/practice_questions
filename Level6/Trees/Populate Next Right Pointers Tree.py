# Given a binary tree
#
#     struct TreeLinkNode {
#       TreeLinkNode *left;
#       TreeLinkNode *right;
#       TreeLinkNode *next;
#     }
# Populate each next pointer to point to its next right node.
# If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
#  Note:
# You may only use constant extra space.
# Example :
#
# Given the following binary tree,
#
#          1
#        /  \
#       2    3
#      / \  / \
#     4  5  6  7
# After calling your function, the tree should look like:
#
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \  / \
#     4->5->6->7 -> NULL
#  Note 1: that using recursion has memory overhead and does not qualify for constant space.
# Note 2: The tree need not be a perfect binary tree.


from Level6.Trees.BinaryTree import BinaryTree, Node


class Solution:

    def solution(self, root):
        current_level = deque()
        next_level = deque()
        current_level.append(root)
        temp = []
        result = []
        while len(current_level) > 0:
            curr_node = current_level[0]
            current_level.popleft()
            if curr_node:
                temp.append(curr_node)
                next_level.append(curr_node.left)
                next_level.append(curr_node.right)
            if len(current_level) == 0:
                if temp:
                    if len(temp) == 1:
                        temp[0]
                    for i in range(0, len(temp)-1):
                        temp[i].next = temp[i+1]
                    temp[-1].next = None
                temp = []
                current_level, next_level = next_level, current_level



