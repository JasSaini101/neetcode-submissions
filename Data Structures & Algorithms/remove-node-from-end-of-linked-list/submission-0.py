# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not (head and head.next):
            return None

        counter, curr = 0, head

        while curr:
            counter += 1
            curr = curr.next

        n = counter - n - 1

        if n < 0:
            head = head.next
            return head

        prev, curr = None, head
        while(n >= 0):
            prev = curr
            curr = curr.next
            n -= 1

        prev.next = curr.next

        return head



        