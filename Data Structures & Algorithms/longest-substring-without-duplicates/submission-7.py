class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # max_length = 0
        # l = 0
        # r = 1

        # while r < len(s):
        #     while s[r] in s[l:r]:
        #         l += 1
        #     max_length = max(max_length, r - l + 1)
        #     r += 1
        
        # return max_length

        max_length = 0
        l = 0
        r = 1

        if len(s) == 0:
            return max_length
        if len(s) == 1:
            return max_length + 1
            
        charset = set(s[l])

        while r < len(s):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            max_length = max(max_length, r - l + 1)
            r += 1
        
        return max_length