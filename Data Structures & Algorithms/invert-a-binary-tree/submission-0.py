class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        suman = root.left
        root.left = root.right
        root.right = suman
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root