class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # l1 = [0] * 26
        # for c in s1:
        #     l1[ord(c) - ord('a')] += 1
        
        # l = 0
        # r = l + len(s1) - 1

        # while r < len(s2):
        #     l2 = [0] * 26
        #     for c in s2[l:r + 1]:
        #         l2[ord(c) - ord('a')] += 1
        #     if l1 == l2:
        #         return True
        #     l += 1
        #     r += 1

        # return False

        l1 = [0] * 26
        for c in s1:
            l1[ord(c) - ord('a')] += 1

        l = 0
        r = len(s1) - 1

        l2 = [0] * 26
        for c in s2[l:r + 1]:
            l2[ord(c) - ord('a')] += 1

        matches = 0

        for count in range(26):
            if l1[count] == l2[count]:
                matches += 1

        if matches == 26:
            return True
        print(matches)
        print(l1)
        print(l2)
        while r < len(s2) - 1:
            l2[ord(s2[l]) - ord('a')] -= 1
            if l1[ord(s2[l]) - ord('a')] - l2[ord(s2[l]) - ord('a')] == 0:
                matches += 1
            elif l1[ord(s2[l]) - ord('a')] - l2[ord(s2[l]) - ord('a')] == 1:
                matches -= 1
            print(matches, l, r, s2[l:r+1])
            print(l1)
            print(l2)
            l += 1
            r += 1
            l2[ord(s2[r]) - ord('a')] += 1
            if l1[ord(s2[r]) - ord('a')] - l2[ord(s2[r]) - ord('a')] == 0:
                matches += 1
            elif l1[ord(s2[r]) - ord('a')] - l2[ord(s2[r]) - ord('a')] == -1:
                matches -= 1
            
            print(matches, l, r, s2[l:r+1])
            print(l1)
            print(l2)
            if matches == 26:
                return True
        
        return False











            