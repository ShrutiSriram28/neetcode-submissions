class TrieNode:
    def __init__(self, val=-1):
        self.children = {}
        self.val = val

class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def createPath(self, path: str, value: int) -> bool:
        path = path.split("/")
        cur = self.root
        
        for i in range(len(path) - 1):
            if path[i] == '':
                continue
            if path[i] not in cur.children:
                return False
            cur = cur.children[path[i]]
        
        if path[-1] in cur.children:
            return False
        
        cur.children[path[-1]] = TrieNode(val=value)
        return True
        
    def get(self, path: str) -> int:
        path = path.split("/")
        cur = self.root

        for p in path:
            if p == '':
                continue
            
            if p not in cur.children:
                return -1
            cur = cur.children[p]
        
        return cur.val


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
