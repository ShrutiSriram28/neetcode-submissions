class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = [0] * 26
        for c in s1:
            l1[ord(c) - ord('a')] += 1
        
        l = 0
        r = l + len(s1) - 1

        while r < len(s2):
            l2 = [0] * 26
            for c in s2[l:r + 1]:
                l2[ord(c) - ord('a')] += 1
            if l1 == l2:
                return True
            l += 1
            r += 1

        return False


            