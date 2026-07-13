class StringIterator:

    def __init__(self, compressedString: str):
        self.comp = compressedString
        self.length = len(compressedString)
        # Stores index of the char it's pointing to right now
        self.char = 0
        # Stores the count of the character that we have gotten 
        self.count = self.getCount(self.char + 1)

    def getCount(self, start):
        count = ''
        if start >= self.length:
            return -1
        while start < self.length and 0 <= ord(self.comp[start]) - ord('0') <= 9:
            count += self.comp[start]
            start += 1
        return int(count)

    def next(self) -> str:
        if self.hasNext():
            self.count -= 1
            return self.comp[self.char]
        return ' '

    def hasNext(self) -> bool:
        if self.count == 0:
            self.char += 1
            while self.char < self.length and 0 <= ord(self.comp[self.char]) - ord('0') <= 9:
                self.char += 1
            self.count = self.getCount(self.char + 1)
        if self.char < self.length:
            return True
        return False


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
