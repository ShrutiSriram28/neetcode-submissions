class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        snew =  ""
        for c in s:
            if c.isalnum() == False:
                continue
            snew += c

        start = 0
        end = len(snew) - 1

        while start < end:
            if snew[start] != snew[end]:
                return False
            start += 1
            end -= 1
        
        return True 