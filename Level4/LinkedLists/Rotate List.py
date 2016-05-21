# Given a list, rotate the list to the right by k places, where k is non-negative.
#
# For example:
#
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.


from Level4.LinkedLists.LinkedList import LinkedList, Node


class Solution:

  @staticmethod
  def solution(head, n):
        if head is None:
            return None
        temp = head
        for i in range(n):
            if temp.next is None:
                temp = head
            else:
                temp = temp.next
        last = head
        while temp.next:
            temp = temp.next
            last = last.next
        temp.next = head
        res = last.next
        last.next = None
        return res

A = LinkedList()
A.add(5)
A.add(4)
A.add(3)
A.add(2)
A.add(1)
A.print()
res = Solution.solution(A.get_root(), 8)
print(res)
