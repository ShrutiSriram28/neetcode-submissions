class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += str(len(i)) + "#" + i
        return s

    def decode(self, s: str) -> List[str]:
        print(s)
        i = 0
        strs = []
        while i < len(s):
            num = ''
            while s[i] != "#":
                num += s[i]
                i += 1
            strs.append(s[i + 1: i + int(num) + 1])
            i += int(num) + 1
        return strs

            
