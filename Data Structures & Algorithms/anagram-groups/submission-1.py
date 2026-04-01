class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        anagramGroups = []

        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord('a')] += 1
            anagrams[tuple(count)] = anagrams.get(tuple(count), [])
            anagrams[tuple(count)].append(word)

        for v in anagrams.values():
            anagramGroups.append(v)

        return anagramGroups