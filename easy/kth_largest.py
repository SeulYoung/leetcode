# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            if root:
                dfs(root.left)
                nums.append(root.val)
                dfs(root.right)

        nums = []
        dfs(root)
        return nums[len(nums) - k]

    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            if self.k and root:
                dfs(root.right)

                self.k -= 1
                if not self.k:
                    self.rtn = root.val
                    return

                dfs(root.left)

        self.k = k
        dfs(root)
        return self.rtn
