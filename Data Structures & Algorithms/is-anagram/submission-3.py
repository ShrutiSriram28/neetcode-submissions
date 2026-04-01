class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = {}
        td = {}
        for c in s:
            sd[c] = sd.get(c, 0) + 1
        for c in t:
            td[c] = td.get(c, 0) + 1
        if len(sd) != len(td):
            return False
        for c in s:
            if sd.get(c) != td.get(c, 0):
                return False
        return True