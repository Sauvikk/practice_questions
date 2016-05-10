# Reverse a linked list from position m to n. Do it in-place and in one-pass.
#
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
#
# return 1->4->3->2->5->NULL.
#
#  Note:
# Given m, n satisfy the following condition:
# 1 ≤ m ≤ n ≤ length of list. Note 2:
# Usually the version often seen in the interviews is reversing the
# whole linked list which is obviously an easier version of this question.
# http://n00tc0d3r.blogspot.in/2013/05/reverse-linked-list.html


from Level4.LinkedLists.LinkedList import LinkedList, Node


class Solution:

  @staticmethod
  def solution(head, m, n):
        dummy = Node(0, head)
        current = head
        prev = dummy
        pos = 1
        while pos < m and current:
            prev = current
            current = current.next
            pos += 1

        while pos < n and current:
            next = current.next.next
            current.next.next = prev.next
            prev.next = current.next
            current.next = next
            pos += 1
        head = dummy.next
        return head

A = LinkedList()
A.add(5)
A.add(4)
A.add(3)
A.add(2)
A.add(1)
res = Solution.solution(A.get_root(), 1, 5)
# res = A.get_root()
while res:
    print(res.val)
    res = res.next



