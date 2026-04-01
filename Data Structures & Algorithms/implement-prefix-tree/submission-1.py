class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.eow = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            ind = ord(c) - ord('a')
            if cur.children[ind] == None: 
                cur.children[ind] = TrieNode()
            cur = cur.children[ind]
        cur.eow = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            ind = ord(c) - ord('a')
            if cur.children[ind] == None:
                return False
            cur = cur.children[ind]
        return cur.eow      # returning cur.eow instead of True because if the word is apple, search(app) should be False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            ind = ord(c) - ord('a')
            if cur.children[ind] == None:
                return False
            cur = cur.children[ind]
        return True
        
        