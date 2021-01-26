# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2: return None
        head_node = head = ListNode(0)
        while l1 and l2:
            if l1.val >= l2.val:
                head_node.next = l2
                l2 = l2.next
            else:
                head_node.next = l1
                l1 = l1.next
            head_node = head_node.next
        if l1!= None:
            head_node.next = l1
        if l2!=None:
            head_node.next = l2
        return head.next
if __name__=='__main__':
    solution=Solution()
    p1=ListNode(1)
    p2=ListNode(2)
    p3=ListNode(3)
    p1.next=p2
    p2.next=p3
    p4 = ListNode(1)
    p5 = ListNode(2)
    p6 = ListNode(3)
    p1.next = p2
    p2.next = p3
    p4.next = p5
    p5.next = p6
    print(solution.mergeTwoLists(p1,p4))