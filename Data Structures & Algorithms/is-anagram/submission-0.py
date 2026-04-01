class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        for c in s:
            if c not in sdict:
                sdict[c] = 1
            else:
                sdict[c] += 1

        tdict = {}
        for c in t:
            if c not in tdict:
                tdict[c] = 1
            else:
                tdict[c] += 1

        if len(sdict) != len(tdict):
            return False
        
        for i in sdict.keys():
            print(i)
            if (i not in tdict.keys()) or (sdict[i] != tdict[i]):
                return False

        return True

        

        