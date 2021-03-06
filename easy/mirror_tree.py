# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return root

    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root:
            stack = [root]
            while stack:
                node = stack.pop()
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                node.left, node.right = node.right, node.left
        return root
