class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        l = 0
        r = 1

        if len(s) <= 1:
            return len(s)
        
        # if len(s) == 2:
        #     if s[0] != s[1]:
        #         return len(s)
        #     else:
        #         return 1

        while r < len(s):
            if s[r] not in s[l:r]:
                r += 1
            else:
                while s[l] != s[r]:
                    l += 1
                l += 1
            length = max(length, r - l)
        
        return length