# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    
        l3 = ListNode(0)
        c = 0
        
        temp = l3
        
        while l1 or l2 or c:
            sum1 = 0
            
            if l1:
                sum1 += l1.val
                l1 = l1.next
                
            if l2:
                sum1 += l2.val
                l2 = l2.next
            
            if c > 0:
                sum1 += c
            
            c = sum1//10
            sum1 %= 10
            temp.next = ListNode(sum1)
            temp = temp.next
            
        return l3.next