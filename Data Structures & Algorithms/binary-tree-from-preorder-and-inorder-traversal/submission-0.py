class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        suman = {}
        for i in range(len(inorder)):
            suman[inorder[i]] = i
        temp = [0]
        def build(left, right):
            if left > right:
                return None
            val = preorder[temp[0]]
            temp[0] += 1
            node = TreeNode(val)
            pos = suman[val]
            node.left = build(left, pos - 1)
            node.right = build(pos + 1, right)
            return node
        return build(0, len(inorder) - 1)