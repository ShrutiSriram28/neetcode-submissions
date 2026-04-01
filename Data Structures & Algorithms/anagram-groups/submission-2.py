class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sd = {}
        for s in strs:
            char = [0] * 26
            for c in s:
                char[ord(c) - ord('a')] += 1
            if tuple(char) not in sd:
                sd[tuple(char)] = [s]
            else:
                sd[tuple(char)].append(s)
        
        anagrams = []
        for v in sd.values():
            anagrams.append(v)
        
        return anagrams