class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        suman = [root]
        ans = []
        while suman:
            temp = []
            ans.append(suman[-1].val)
            for node in suman:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            suman = temp
        return ans