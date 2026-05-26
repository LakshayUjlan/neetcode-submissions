# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3=ListNode()
        s1,s2,s3=list1,list2,list3
        while s1 and s2:
            if s1.val <= s2.val:
                s3.next=ListNode(s1.val)
                s1=s1.next
            else:
                s3.next=ListNode(s2.val)
                s2=s2.next
            s3=s3.next
        while s1 :
            s3.next=ListNode(s1.val)
            s1=s1.next
            s3=s3.next
        while s2 :
            s3.next=ListNode(s2.val)
            s2=s2.next
            s3=s3.next
        return list3.next

        