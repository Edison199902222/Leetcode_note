# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
这道题跟链表中倒数第k个节点 有点像 但不全是
首先要在链表首 插入一个dummy
然后 建立两个指针 指向dummy
fast 指针先移动n次
然后两个指针同时移动
这样slow指针就是我们要移除指针的前一个
再把slow的next设置为next next就好
'''
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head: return None
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy
        while n > 0:
            fast = fast.next
            n-=1
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
