class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
# @param head ListNode类
# @return bool布尔型
#
class Solution:
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    def hasCycle(self, head):
        node_set = set()
        while head:
            if head in node_set:
                return True
            node_set.add(head)
            head = head.next
        return False

    def hasCycle(self, head):
        while head and head.next:
            if head.next == head:
                return True
            # tmp = head.next
            # head.next = head
            # head = tmp
            head.next, head = head, head.next
        return False
