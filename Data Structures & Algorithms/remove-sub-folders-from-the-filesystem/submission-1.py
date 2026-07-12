class TrieNode:
    def __init__(self):
        self.children = {}
        self.folder = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, folder):
        folder = folder.split("/")
        cur = self.root
        
        for c in folder:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.folder = True
    
    def search(self, folder):
        folder = folder.split("/")
        cur = self.root

        for i in range(len(folder) - 1):
            if cur.children[folder[i]].folder:
                return False
            cur = cur.children[folder[i]]
        return True

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        prefix = PrefixTree()
        for f in folder:
            prefix.insert(f)

        res = []
        for f in folder:
            if prefix.search(f):
                res.append(f)

        return res
