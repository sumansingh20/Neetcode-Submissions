class Solution:
    def isValidBST(self, root):
        def suman(node, left, right):
            if node == None:
                return True
            if node.val <= left or node.val >= right:
                return False
            a = suman(node.left, left, node.val)
            b = suman(node.right, node.val, right)
            return a and b
        return suman(root, -999999999, 999999999)