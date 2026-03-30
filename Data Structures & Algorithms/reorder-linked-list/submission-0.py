# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # found the mid point now
        prevptr = None
        curptr = slow.next # you actually reverse the second half
        slow.next = None
        while curptr:
            nextptr = curptr.next
            curptr.next = prevptr
            prevptr = curptr
            curptr = nextptr

        # second half has been reversed now. prevptr is the last node
        left = head

        right = prevptr

        while right:
            left_next = left.next
            right_next = right.next
            left.next = right
            right.next = left_next
            left = left_next
            right = right_next





