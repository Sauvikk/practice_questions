# Given a linked list, remove the nth node from the end of list and return its head.
#
# For example,
# Given linked list: 1->2->3->4->5, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.
#
#  Note:
# * If n is greater than the size of the list, remove the first node of the list.
# Try doing it using constant additional space.
# http://yucoding.blogspot.in/2013/04/leetcode-question-82-remove-nth-node.html
# http://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/


from Level4.LinkedLists.LinkedList import LinkedList, Node


class Solution:

  @staticmethod
  def solution(head, n):
        if head is None:
            return None
        temp = head
        for i in range(n):
            if temp.next is None:
                head = head.next
                return head
            else:
                temp = temp.next
        last = head
        while temp.next:
            temp = temp.next
            last = last.next
        last.next = last.next.next
        return head

A = LinkedList()
A.add(5)
A.add(4)
A.add(3)
A.add(2)
A.add(1)
A.print()
res = Solution.solution(A.get_root(), 2)
LinkedList.print_any(res)

