
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
            
            num1 = '' 
            curr1 = l1
            while curr1 is not None:
                num1 += str(curr1.val)
                curr1 = curr1.next
            
            num2 = '' 
            curr2 = l2    
            while curr2 is not None:
                num2 += str(curr2.val)
                curr2 = curr2.next
                
            sum_result = [int(i) for i in str(int(num1[::-1]) + int(num2[::-1]))]
        
            head = None
            for i in sum_result:
                node = ListNode(i)
                node.next = head
                head = node
                
            return head
#changes in GitHub
