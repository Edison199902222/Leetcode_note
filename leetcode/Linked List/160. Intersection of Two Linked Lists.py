# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
两个链表 两个指针 p1 p2
都是从头开始走 如果任何一个指针 指到None
然后就从另一个链表的开头走 直到相遇就return
原理就是 如果两个链表 合起来
两个指针 其实走的路是一样多的 因为走到空 就换一个链表走

'''
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        while p1 != p2:
            if not p1:
                p1 = headB
            else:
                p1 = p1.next
            if not p2:
                p2 = headA
            else:
                p2 = p2.next
        return p2
