# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result_head = ListNode()
        result_node = result_head
        carry_over = 0
        
        while l1 or l2 or carry_over:
            val1 = l1.val if l1 else 0 
            val2 = l2.val if l2 else 0
            
            # Soma dos valores dos nós e do carry
            sum = val1 + val2 + carry_over
            
            # Calcula o novo carry para a próxima soma
            carry_over = sum // 10
            
             # Calcula o dígito a ser adicionado ao resultado
            digit = sum % 10
            
            result_node.next = ListNode(digit)
            result_node = result_node.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return result_head.next
