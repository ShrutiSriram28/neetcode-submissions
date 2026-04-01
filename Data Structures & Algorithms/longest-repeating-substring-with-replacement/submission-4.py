class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        length = 0
        freq = {}

        while r < len(s):
            freq[s[r]] = 1 + freq.get(s[r], 0)

            if r - l + 1 - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            
            length = max(length, r - l + 1)
            r += 1
        
        return length



