class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
# @param pHead ListNode类
# @param k int整型
# @return ListNode类
#
class Solution:
    def FindKthToTail(self, pHead, k):
        if k <= 0:
            return None

        node_list = []
        while pHead:
            node_list.append(pHead)
            pHead = pHead.next

        if len(node_list) < k:
            return None
        return node_list[len(node_list) - k]

    def FindKthToTail(self, pHead, k):
        if k <= 0:
            return None

        fast, slow = pHead, pHead
        idx = k
        while idx:
            if not fast:
                return None
            fast = fast.next
            idx -= 1

        while fast:
            fast = fast.next
            slow = slow.next
        return slow
