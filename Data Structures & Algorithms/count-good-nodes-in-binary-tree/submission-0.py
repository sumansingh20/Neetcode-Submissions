class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def suman(node, temp):
            if not node:
                return 0
            count = 0
            if node.val >= temp:
                count = 1
                temp = node.val
            count += suman(node.left, temp)
            count += suman(node.right, temp)
            return count
        return suman(root, root.val)