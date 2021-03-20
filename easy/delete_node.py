# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteNode(node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    pre_node = None
    while node.next:
        next_node = node.next
        node.val = next_node.val
        pre_node = node
        node = next_node
    pre_node.next = None


def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next
