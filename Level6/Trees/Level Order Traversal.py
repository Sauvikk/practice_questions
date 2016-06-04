# http://articles.leetcode.com/printing-binary-tree-in-level-order
# http://www.geeksforgeeks.org/level-order-tree-traversal/

from Level6.Trees.BinaryTree import BinaryTree, Node
from collections import deque


class Solution:

    def solution(self, root):
        if not root:
            return
        current_level = deque()
        next_level = deque()
        current_level.append(root)
        temp = []
        result = []
        while len(current_level) > 0:
            curr_node = current_level[0]
            current_level.popleft()
            if curr_node:
                temp.append(curr_node.val)
                next_level.append(curr_node.left)
                next_level.append(curr_node.right)
            if len(current_level) == 0:
                if temp:
                    result.append(temp)
                temp = []
                current_level, next_level = next_level, current_level
        return result

node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.left.right = Node(5)
node.right.left = Node(6)
node.right.right = Node(7)
node.left.left.left = Node(8)
node.left.left.right = Node(9)
node.right.right.left = Node(10)
node.right.right.right = Node(11)
res = Solution().solution(node)
print(res)
