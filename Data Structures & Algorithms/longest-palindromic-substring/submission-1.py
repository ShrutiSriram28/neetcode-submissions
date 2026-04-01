class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
            
        res = ""
        reslen = 0

        i = 0
        while i < len(s) - 1:
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > reslen:
                    reslen = r - l + 1
                    res = s[l:r + 1]
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > reslen:
                    reslen = r - l + 1
                    res = s[l: r + 1]
                l -= 1
                r += 1
            i += 1

        return res