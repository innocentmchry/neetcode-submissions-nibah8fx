# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Let me try the two iteration solution myself

        total = 0
        cur = head
        while cur:
            total += 1
            cur = cur.next

        target = total - n
        if target == 0:
            return head.next

        count = 0
        cur = head
        while cur:
            count += 1
            if count == target:
                if cur.next:
                    cur.next = cur.next.next
                else:
                    cur.next = None
            
            cur = cur.next

        return head
