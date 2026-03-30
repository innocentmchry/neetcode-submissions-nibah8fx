# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Using hashset

        my_hashset = set()

        while head:
            if head in my_hashset:
                return True
            else:
                my_hashset.add(head)
                head = head.next
        
        return False
