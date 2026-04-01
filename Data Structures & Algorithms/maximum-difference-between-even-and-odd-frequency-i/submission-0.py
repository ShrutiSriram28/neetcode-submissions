class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}

        for c in s:
            freq[c] = freq.get(c, 0) + 1

        max_odd = float("-inf")
        min_even = float("inf")
        for k, v in freq.items():
            if v % 2 == 1 and v > max_odd:
                max_odd = v
            elif v % 2 == 0 and v < min_even:
                min_even = v
        
        return max_odd - min_even