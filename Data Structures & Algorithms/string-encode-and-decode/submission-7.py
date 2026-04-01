class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_str += str(len(word)) + "#" + word 
        return encoded_str

    def decode(self, s: str) -> List[str]:
        str = []
        i = 0

        while i < len(s):
            length = ""
            word = ""
            while s[i] != '#':
                length += s[i]
                i += 1
            start = i + 1
            end = i + 1 + int(length)
            for j in range(start, end):
                word += s[j]
                i = j
            str.append(word)
            i += 1

        return str

