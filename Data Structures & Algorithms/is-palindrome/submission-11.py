class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s1 = ""

        for c in s:
            if (ord(c) < ord('0') or ord(c) > ord('9')) and (ord(c) < ord('a') or ord(c) > ord('z')):
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