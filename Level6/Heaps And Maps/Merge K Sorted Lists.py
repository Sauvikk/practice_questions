# Merge k sorted linked lists and return it as one sorted list.
#
# Example :
#
# 1 -> 10 -> 20
# 4 -> 11 -> 13
# 3 -> 8 -> 9
# will result in
#
# 1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20


from Level4.LinkedLists.LinkedList import Node


class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        lists = A
        vals = []
        for head in lists:
            while head is not None:
                vals.append(head.val)
                head = head.next
        vals.sort()
        head = Node(vals[0])
        itr = head
        for i in vals[1:]:
            itr.next = Node(i)
            itr = itr.next
        return head

