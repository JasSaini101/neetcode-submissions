# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr, least = head, head.val
        while(curr.next != None):
            curr = curr.next
            if(curr.val <= least):
                return True
            least = curr.val
        return False

        