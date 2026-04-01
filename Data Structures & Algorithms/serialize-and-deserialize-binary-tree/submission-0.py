# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ser = []
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                ser.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                ser.append("N")
        return ",".join(ser)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        q = deque()
        ser = data.split(",")
        i = 0
        if ser[i] == "N":
            return None
        root = TreeNode(int(ser[i]), None, None)
        i += 1
        q.append(root)
        while q:
            node = q.popleft()
            if ser[i] != "N":
                node.left = TreeNode(int(ser[i]), None, None)
                q.append(node.left)
            i += 1
            if ser[i] != "N":
                node.right = TreeNode(int(ser[i]), None, None)
                q.append(node.right)
            i += 1
        return root