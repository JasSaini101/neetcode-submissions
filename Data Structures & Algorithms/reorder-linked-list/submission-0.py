# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next or not head.next.next:
            return

        temp, store, prev, curr = head, head.next, head, head.next

        while(temp.next):

            while(curr.next):
                prev = curr
                curr = curr.next

            if prev == temp:
                return

            prev.next = curr.next #might give error
            temp.next = curr
            curr.next = store

            temp = store
            store = store.next



        