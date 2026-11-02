class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        ans = []
        st = [root]
        
        while st:
            curr = st.pop()
            ans.append(curr.val)
            
            if curr.right:
                st.append(curr.right)
            if curr.left:
                st.append(curr.left)
        return ans