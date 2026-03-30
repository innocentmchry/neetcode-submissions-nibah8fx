# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        no_of_nodes = 0
        cur = head
        while cur:
            no_of_nodes += 1
            cur = cur.next

        pos = no_of_nodes - n
        if pos == 0:
            return head.next
        count = 0
        cur = head
        while cur:
            count += 1
            if count == pos:
                cur.next = cur.next.next

            cur = cur.next

        return head