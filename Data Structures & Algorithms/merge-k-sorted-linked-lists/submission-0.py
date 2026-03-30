# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        cur_min_idx = -1

        dummy = ListNode()
        curr = dummy

        def all_null(ls):
            for i in range(len(lists)):
                if ls[i] != None:
                    return True

            return False

        while all_null(lists):

            cur_min = 9999

            for i, sorted_ll in enumerate(lists):
                if lists[i] != None and lists[i].val < cur_min:
                    cur_min = lists[i].val
                    cur_min_idx = i
            
            lists[cur_min_idx] = lists[cur_min_idx].next

            curr.next = ListNode(cur_min)
            curr = curr.next

        return dummy.next


            

            
