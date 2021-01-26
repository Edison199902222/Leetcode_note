# Definition for singly-linked list.
'''
要分成两个函数
主函数 先找到中间节点 然后分成两个list
然后递归拆开 用merge合并
merge 就是用来合并两个链表
最后return head就行
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        fast, slow = head, head
        while fast.next is not None and fast.next.next is not None:
            fast, slow = fast.next.next, slow.next
        l1 = head
        l2 = slow.next
        slow.next = None
        head1 = self.sortList(l1)
        head2 = self.sortList(l2)
        head = self.merge(head1, head2)
        return head

    def merge(self, l1, l2):
        if l1 is None: return l2
        if l2 is None: return l1
        dummy = ListNode(0)
        p = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
                p = p.next
            else:
                p.next = l2
                l2 = l2.next
                p = p.next
        if l1 is not None:
            p.next = l1
        if l2 is not None:
            p.next = l2
        return dummy.next
if __name__=='__main__':
    solution=Solution()
    p1=ListNode(4)
    p2=ListNode(2)
    p3 = ListNode(1)
    p4 = ListNode(3)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    print(solution.sortList(p1))