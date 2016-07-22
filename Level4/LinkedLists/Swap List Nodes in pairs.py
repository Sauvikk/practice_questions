# Given a linked list, swap every two adjacent nodes and return its head.
#
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Your algorithm should use only constant space. You may not modify the values in the list,
#  only nodes itself can be changed.


from Level4.LinkedLists.LinkedList import LinkedList, Node


class Solution:

    @staticmethod
    def solution(head):
        dummy_head = Node(0)
        dummy_head.next = head
        current = dummy_head
        while current.next and current.next.next:
            current.next = Solution.swap(current.next, current.next.next)
            current = current.next.next
        return dummy_head.next

    @staticmethod
    def swap(node1, node2):
        node1.next = node2.next
        node2.next = node1
        return node2

A = LinkedList()
A.add(0)
A.add(2)
A.print()
res = Solution.solution(A.get_root())
LinkedList.print_any(res)
