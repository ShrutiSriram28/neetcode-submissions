class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = {}
        wordList.append(beginWord)
        for w in wordList:
            for j in range(len(w)):
                pattern = w[:j] + "*" + w[j + 1:]
                if pattern not in nei:
                    nei[pattern] = [w]
                else:
                    nei[pattern].append(w)
        
        visited = set(beginWord)
        res = 1
        q = deque([beginWord])

        while q:
            for i in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return res
                for j in range(len(w)):
                    pattern = w[:j] + "*" + w[j + 1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visited:
                            visited.add(neiWord)
                            q.append(neiWord)
            res += 1
        
        return 0