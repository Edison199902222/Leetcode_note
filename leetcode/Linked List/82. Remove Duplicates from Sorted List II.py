# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
在链表前插入dummy 并 current = dummy
然后检查 如果current的下一个 跟下下个相等 那么val = current next 的val 那么就用while循环 把current的指针指向下下个
如果不相等的话 则 = 下一个node
'''
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        current_node = dummy
        while current_node.next is not None and current_node.next.next is not None:
            if current_node.next.val == current_node.next.next.val:
                val = current_node.next.val
                while current_node.next is not None and current_node.next.val == val:
                    current_node.next = current_node.next.next
            else:
                current_node = current_node.next
        return dummy.next