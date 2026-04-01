class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        patterns = {}
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                if pattern not in patterns:
                    patterns[pattern] = [word]
                else:
                    patterns[pattern].append(word)

        print(patterns)

        length = 1
        q = deque([beginWord])
        visit = set([beginWord])
        while q:
            for j in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return length
                print("Word:", word)
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    print("**", pattern, patterns[pattern])
                    for nei in patterns[pattern]:
                        if nei not in visit:
                            q.append(nei)
                            visit.add(nei)
            length += 1

        return 0