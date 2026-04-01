class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for i in strs:
            count = [0] * 26
            for c in i:
                count[ord(c) - ord('a')] += 1
            if anagrams.get(tuple(count), 0) == 0:
                anagrams[tuple(count)] = [i]
            else:
                anagrams[tuple(count)].append(i)
        
        anagram_list = []
        for i in anagrams.values():
            anagram_list.append(i)
        
        return anagram_list

