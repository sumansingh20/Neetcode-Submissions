class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        st = []
        cur = root
        
        while cur != None or len(st) > 0:
            while cur != None:
                st.append(cur)
                cur = cur.left
            cur = st.pop()
            ans.append(cur.val)
            cur = cur.right
            
        return ans