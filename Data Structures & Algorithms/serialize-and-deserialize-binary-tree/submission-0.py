class Codec:
    def serialize(self, root):
        suman = []
        def temp(node):
            if not node:
                suman.append("N")
                return
            suman.append(str(node.val))
            temp(node.left)
            temp(node.right)
        temp(root)
        return ",".join(suman)
    def deserialize(self, data):
        suman = data.split(",")
        temp = [0]
        def build():
            if suman[temp[0]] == "N":
                temp[0] += 1
                return None
            node = TreeNode(int(suman[temp[0]]))
            temp[0] += 1
            node.left = build()
            node.right = build()
            return node
        return build()