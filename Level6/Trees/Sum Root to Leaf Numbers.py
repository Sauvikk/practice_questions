# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
#
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers % 1003.
#
# Example :
#
#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
#
# Return the sum = (12 + 13) % 1003 = 25 % 1003 = 25.


from Level6.Trees.BinaryTree import BinaryTree, Node


class Solution:

    def generate_sum(self, node, num, sum):
        if node is None:
            return sum
        num = (num*10 + node.val) % 1003
        if node.left is None and node.right is None:
            sum += num
            return sum % 1003
        return self.generate_sum(node.left, num, sum) + self.generate_sum(node.right, num, sum)

    def solution(self, root):
        if root is None:
            return 0
        return self.generate_sum(root, 0, 0) % 1003


# root = Node(5)
# root.left = Node(4)
# root.left.left = Node(11)
# root.left.left.left = Node(7)
# root.left.left.right = Node(2)
# root.right = Node(8)
# root.right.right = Node(4)
# root.right.left = Node(13)
# root.right.right.right = Node(1)
# root.right.right.left = Node(5)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
res = Solution().solution(root)
print(res)
