# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
用一个快慢指针 加上rev指针去写
快 指针每次移动 两格 慢指针每次移动一个 同时 把rev 每一次都逆向指向自己 并且更新为slow
比如 1 -> 2 -> 3  rev第一次等于1 然后指向之前的自己 就是 1 -> None, 2 -> 1 -> None
要注意 如果链表是奇数的时候， slow 还需要移动一次才可以指向我们要比较的第一个node
最后 比较rev 与 slow相等不相等就行
'''
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rev = None
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev:
            if rev.val != slow.val:
                return False
            slow, rev = slow.next, rev.next
        return True
