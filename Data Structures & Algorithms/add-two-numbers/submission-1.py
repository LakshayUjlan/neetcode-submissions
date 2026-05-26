# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
       l3=ListNode()
       start1,start2,start3=l1,l2,l3
       carry=0
       while start1 or start2 or carry:
        val1 = start1.val if start1 else 0
        val2 = start2.val if start2 else 0
        total = val1+val2+carry
        carry = total//10
        digit = total%10
        start3.next=ListNode(digit)
        start3=start3.next
        if start1:
            start1=start1.next
        if start2:
            start2=start2.next
       return l3.next