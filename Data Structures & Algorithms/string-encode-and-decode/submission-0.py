class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += i + "^#$"
        return s

    def decode(self, s: str) -> List[str]:
        strs = s.split("^#$")[:-1]
        return strs
