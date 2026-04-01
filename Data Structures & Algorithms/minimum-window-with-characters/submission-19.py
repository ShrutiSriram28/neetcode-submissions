class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return t

        sub, window = {}, {}
        for c in t:
            sub[c] = sub.get(c, 0) + 1

        l = 0
        need = len(t)
        sub_string = [0, 0]
        length = len(s) + 1

        for r in range(len(s)):
            if s[r] in sub:
                window[s[r]] = window.get(s[r], 0) + 1
                if window[s[r]] <= sub[s[r]]:
                    need -= 1
                    
            while need == 0:
                if r - l + 1 < length:
                    length = r - l + 1
                    sub_string = [l, r]
                if s[l] in sub:
                    window[s[l]] -= 1
                    if window[s[l]] < sub[s[l]]:
                        need += 1
                l += 1
                
        l, r = sub_string 
        if length != len(s) + 1:
            return s[l: r + 1]
        else:
            return ""