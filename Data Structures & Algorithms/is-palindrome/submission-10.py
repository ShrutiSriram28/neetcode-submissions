class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s1 = ""

        for c in s:
            if (ord(c) < 48 or ord(c) > 57) and (ord(c) < 97 or ord(c) > 122):
                continue
            s1 += c
        
        l = 0
        r = len(s1) - 1

        while r > l:
            if s1[l] != s1[r]:
                return False
            l += 1
            r -= 1

        return True