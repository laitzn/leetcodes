# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        atual = dummy
        passa_um = 0

        while l1 or l2 or passa_um:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            soma_total = val1 + val2 + passa_um
            
            passa_um = soma_total // 10
            
            atual.next = ListNode(soma_total % 10)

            atual = atual.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next