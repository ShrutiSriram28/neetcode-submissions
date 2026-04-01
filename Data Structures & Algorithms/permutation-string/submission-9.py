class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sub_count = [0] * 26
        window = [0] * 26

        if len(s1) > len(s2):
            return False

        for c in s1:
            sub_count[ord(c) - ord('a')] += 1

        l = 0
        r = len(s1) - 1

        for i in range(l, r + 1):
            window[ord(s2[i]) - ord('a')] += 1

        match_count = 0

        for i in range(26):
            if sub_count[i] == window[i]:
                match_count += 1
        
        if match_count == 26:
            return True

        l += 1
        r += 1
    
        while r < len(s2):
            window[ord(s2[l - 1]) - ord('a')] -= 1
            if sub_count[ord(s2[l - 1]) - ord('a')] == window[ord(s2[l - 1]) - ord('a')]:
                match_count += 1
            elif sub_count[ord(s2[l - 1]) - ord('a')] == window[ord(s2[l - 1]) - ord('a')] + 1:
                match_count -= 1

            window[ord(s2[r]) - ord('a')] += 1
            if sub_count[ord(s2[r]) - ord('a')] == window[ord(s2[r]) - ord('a')]:
                match_count += 1
            elif sub_count[ord(s2[r]) - ord('a')] == window[ord(s2[r]) - ord('a')] - 1:
                match_count -= 1

            if match_count == 26:
                return True

            l += 1
            r += 1

        return False