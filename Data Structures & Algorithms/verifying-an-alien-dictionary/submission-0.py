class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = {order[i]:i for i in range(len(order))}

        for i in range(len(words) - 1):
            n = min(len(words[i]), len(words[i + 1]))
            flag = False
            for j in range(n):
                if mapping[words[i][j]] < mapping[words[i + 1][j]]:
                    flag = True
                    break
                elif mapping[words[i][j]] > mapping[words[i + 1][j]]:
                    return False
            if len(words[i]) > len(words[i + 1]) and flag == False:
                return False

        return True