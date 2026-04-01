class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for s in strs:
                if i >= len(s) or s == "" or s[i] != c:
                    return common
            common += c
        return common