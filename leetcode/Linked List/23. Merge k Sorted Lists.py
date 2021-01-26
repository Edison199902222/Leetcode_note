# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
用merge sort去做
先把list 拆成一个一个
然后每次调用merge 去合并
最后返回
So it iterates over the linked lists lg(N) times, making the time complexity O(M*lg(N)), where M is the size of the merged linked list and N is the size of the lists argument.
Space complexity with recursion stack is O(lg(N)), without recursion stack is O(1)
'''

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists: return
        if len(lists) == 1:
            return lists[0]
        mid = len(lists)//2
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])
        return self.merge(l, r)
    def merge(self,l,r):
        dummy = cur =  ListNode(0)
        while l and r:
            if l.val < r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        if l is not None:
            cur.next = l
        if r is not None:
            cur.next = r
        return dummy.next

