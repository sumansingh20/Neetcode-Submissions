class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        suman = [-10**9]
        def temp(node):
            if not node:
                return 0
            left = max(0, temp(node.left))
            right = max(0, temp(node.right))
            suman[0] = max(suman[0], left + right + node.val)
            return max(left, right) + node.val
        temp(root)
        return suman[0]