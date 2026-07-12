class TrieNode:
    def __init__(self, isFolder=False, content=''):
        self.children = {}
        self.isFolder = isFolder
        self.content = content

class FileSystem:

    def __init__(self):
        self.root = TrieNode(isFolder=True)

    def ls(self, path: str) -> List[str]:
        cur = self.root
        folders = path.split("/")

        for folder in folders:
            if folder == '':
                continue
            cur = cur.children[folder]

        ls_ret = []
        if cur.isFolder:
            for doc in cur.children:
                # doc = "/".join(doc)
                ls_ret.append(doc)
        else:
            return [folders[-1]]
    
        return sorted(ls_ret)

    def mkdir(self, path: str) -> None:
        folders = path.split('/')

        cur = self.root

        for folder in folders:
            if folder == '':
                continue
            if folder not in cur.children:
                cur.children[folder] = TrieNode(isFolder=True)
            cur = cur.children[folder]
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        folders = filePath.split('/')

        cur = self.root

        for i in range(len(folders) - 1):
            if folders[i] == '':
                continue
            if folders[i] not in cur.children:
                cur.children[folders[i]] = TrieNode(isFolder=True)
            cur = cur.children[folders[i]]
        if folders[-1] not in cur.children:
            cur.children[folders[-1]] = TrieNode(content=content)
        else:
            cur = cur.children[folders[-1]]
            cur.content += content

    def readContentFromFile(self, filePath: str) -> str:
        cur = self.root
        folders = filePath.split('/')

        for folder in folders:
            if folder == '':
                continue
            cur = cur.children[folder]
        return cur.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
