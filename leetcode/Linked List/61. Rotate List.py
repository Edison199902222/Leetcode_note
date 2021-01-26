# Definition for singly-linked list.
'''
两个指针 fast and slow
让fast先走k%length 步
然后 我们需要同时走
让fast 指向链表尾部 slow也会走
停止时 slow 就是新的队尾 会指向None slow的下一个就是new head fast 的下一个会指向头
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None: return head
        length = 0
        new_head = head
        slow, fast = head,head
        while new_head is not None:
            length += 1
            new_head = new_head.next
        for i in range(k % length):
            fast = fast.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        fast.next = head
        head = slow.next
        slow.next = None
        return head
if __name__=='__main__':
    solution=Solution()
    p1=ListNode(1)
    print(solution.rotateRight(p1,0))