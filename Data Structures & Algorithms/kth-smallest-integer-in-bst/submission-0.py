class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        suman = []
        def temp(node):
            if not node:
                return
            temp(node.left)
            suman.append(node.val)
            temp(node.right)
        temp(root)
        return suman[k - 1]