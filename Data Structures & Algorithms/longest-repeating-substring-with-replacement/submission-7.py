class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        l = 0
        r = 0
        chars = {}
        max_char = s[r]
        
        while r < len(s):
            chars[s[r]] = chars.get(s[r], 0) + 1
            if chars[s[r]] > chars[max_char]:
                max_char = s[r] 
            if r - l + 1 - chars[max_char] > k:
                chars[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
            r += 1

        return max_length