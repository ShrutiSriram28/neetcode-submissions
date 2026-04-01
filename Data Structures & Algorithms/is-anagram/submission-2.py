class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sdict = {}
        tdict = {}

        for sc in s:
            sdict[sc] = sdict.get(sc, 0) + 1
        
        for tc in t:
            tdict[tc] = tdict.get(tc, 0) + 1

        if len(sdict) != len(tdict):
            return False
        
        for c in sdict:
            if sdict.get(c) != tdict.get(c, -1):
                return False

        return True
        