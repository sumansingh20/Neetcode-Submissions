class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        a=[root]
        ans=[]
        while a:
            node=a.pop()
            ans.append(node.val)
            if node.left:
                a.append(node.left)
            if node.right:
                a.append(node.right)
        return ans[::-1]