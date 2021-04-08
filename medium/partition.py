# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small = small_head = ListNode(0)
        large = large_head = ListNode(0)
        while head:
            if head.val < x:
                small.next = small = head
            else:
                large.next = large = head
            head = head.next

        large.next = None
        small.next = large_head.next
        return small_head.next
