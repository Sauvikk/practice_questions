# Given a singly linked list
#
#     L: L0 → L1 → … → Ln-1 → Ln,
# reorder it to:
#
#     L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
# You must do this in-place without altering the nodes’ values.
#
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.


from Level4.LinkedLists.LinkedList import LinkedList, Node


class Solution:
        def reverse_list(self, head):
            prev = None
            curr = head
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev

        def solution(self, head):

            slow = head
            fast = slow.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            head1 = head
            head2 = slow.next
            slow.next = None
            head2 = self.reverse_list(head2)

            head = Node(0)
            curr = head

            while head1 or head2:
                if head1:
                    curr.next = head1
                    curr = curr.next
                    head1 = head1.next
                if head2:
                    curr.next = head2
                    curr = curr.next
                    head2 = head2.next
            head = head.next
            return head

A = LinkedList()
A.add(4)

A.print()
res = Solution().solution(A.get_root())
LinkedList.print_any(res)
