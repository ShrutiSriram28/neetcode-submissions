class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False
    
class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.eow = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        prefix = PrefixTree()
        for word in words:
            prefix.insert(word)
        
        rows = len(board)
        cols = len(board[0])
        visited, res = set(), set()

        def dfs(r, c, node, word):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or board[r][c] not in node.children:
                return False

            visited.add((r, c))
            word += board[r][c]
            node = node.children[board[r][c]]

            if node.eow:
                res.add(word)

            dfs(r - 1, c, node, word) 
            dfs(r + 1, c, node, word)  
            dfs(r, c - 1, node, word) 
            dfs(r, c + 1, node, word) 
            
            visited.remove((r, c))
            
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, prefix.root, '')
                
        return list(res)