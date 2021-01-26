# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
用dummy 插入
然后有三个指针 pre m n
pre 是m 前一个指针
先让 pre 跟 m 走到位置
然后让n 也走到 位置
然后每次让m 插入到n的后面 同时 m每次都是pre的下一个
直到m与n重合 就说明reverse 完了
'''
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None: return head
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        m_node = head
        n_node = head
        for i in range(1,m):
            pre = pre.next
            m_node = m_node.next
        for i in range(1,n):
            n_node = n_node.next
        while n_node != m_node:
            pre.next = m_node.next
            m_node.next = n_node.next
            n_node.next = m_node
            m_node = pre.next
        return dummy.next