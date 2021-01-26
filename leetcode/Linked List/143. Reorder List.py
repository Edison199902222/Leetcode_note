# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
拆分成三个部分去解决
先用findmid  去找到中间node
然后 把list 拆成两个部分
然后把后半部分 反转
然后再进行合并 
'''
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None: return None
        mid = self.findmid(head)
        l2 = mid.next
        mid.next = None
        l2 = self.reverse(l2)
        l1 = head
        while l1 is not None and l2 is not None:
            next = l1.next
            l1.next = l2
            l2 = l2.next
            l1.next.next = next
            l1 = next

    def findmid(self, head):
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow, fast = slow.next, fast.next.next
        return slow

    def reverse(self, head):
        pre = None
        cur = head
        while cur is not None:
            cur.next, pre, cur = pre, cur, cur.next
        return pre
