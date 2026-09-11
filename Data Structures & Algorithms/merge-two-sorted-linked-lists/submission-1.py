# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2, head = list1, list2, ListNode()

        if(p1 == None):
            return(p2)
        
        if(p2 == None):
            return(p1)

        if p1.val < p2.val:
            head = p1
            p1 = p1.next
        else:
            head = p2
            p2 = p2.next

        answer = head

        while(p1 != None and p2 != None):
            if(p1.val <= p2.val):
                answer.next = p1
                p1 = p1.next
            else:
                answer.next = p2
                p2 = p2.next
            answer = answer.next

        if(p1 == None):
            while(p2 != None):
                answer.next = p2
                answer = answer.next
                p2 = p2.next
        
        if(p2 == None):
            while(p1 != None):
                answer.next = p1
                answer = answer.next
                p1 = p1.next
                

        return(head)


    