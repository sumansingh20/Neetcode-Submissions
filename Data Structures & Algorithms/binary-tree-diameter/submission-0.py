class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        suman = 0
        def temp(node):
            nonlocal suman
            if not node:
                return 0
            left = temp(node.left)
            right = temp(node.right)
            suman = max(suman, left + right)
            return max(left, right) + 1
        temp(root)
        return suman