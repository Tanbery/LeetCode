# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def listnode_to_str(self,lstNode:ListNode):
        ret = '' 
        cur = lstNode
        while curr1 is not None:
            ret += str(cur.val)
            cur = cur.next
        return ret

    def list_to_listnode(self,lst):
        head = None
        for i in lst:
            node = ListNode(i)
            node.next = head
            head = node
        return head

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
            
            num1 =  listnode_to_str(l1)
            num2 =  listnode_to_str(l2)
                
            sum_result = [int(i) for i in str(int(num1[::-1]) + int(num2[::-1]))]
            
            return list_to_listnode(sum_result)
                                  
            return list_to_listnode(sum_result)

#changes in GitHub
