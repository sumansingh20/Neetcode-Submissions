class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        suman = [root]
        ans = []
        while suman:
            temp = []
            data = []
            for node in suman:
                data.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            ans.append(data)
            suman = temp
        return ans