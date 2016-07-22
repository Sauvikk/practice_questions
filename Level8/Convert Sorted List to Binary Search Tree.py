# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
#
#  A height balanced BST : a height-balanced binary tree is defined
#  as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
# Example :
#
#
# Given A : 1 -> 2 -> 3
# A height balanced BST  :
#
#       2
#     /   \
#    1     3


from Level4.LinkedLists.LinkedList import LinkedList, Node as List_Node
from Level6.Trees.BinaryTree import BinaryTree, Node


class Solution:
    def __init__(self):
        self.h = List_Node(0)

    def sol(self, head):
        if head is None:
            return None
        self.h = head
        length = self.get_lenght(head)
        return self.sort_list_to_bst(0, length - 1)

    def get_lenght(self, head):
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        return length

    def sort_list_to_bst(self, start, end):
        if start > end:
            return None
        mid = int((start + end) / 2)
        left = self.sort_list_to_bst(start, mid - 1)
        root = Node(self.h.val)
        self.h = self.h.next
        right = self.sort_list_to_bst(mid + 1, end)
        root.left = left
        root.right = right
        return root


x = List_Node(1)
x.next = List_Node(2)
x.next.next = List_Node(3)
y = Solution().sol(x)
BinaryTree().in_order(y)
