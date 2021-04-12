class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
# @param head ListNode类
# @return ListNode类
#
class Solution:
    def detectCycle(self, head):
        while head and head.next:
            if head.next == head:
                return head
            head.next, head = head, head.next
        return None

    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                p_head = head
                while (p_head != slow):
                    p_head = p_head.next
                    slow = slow.next
                return slow
        return None


l = ListNode(1)
l.next = ListNode(2)
s = Solution()
s.detectCycle(l)
