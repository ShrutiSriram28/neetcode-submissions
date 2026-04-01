class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = []
        
        while n > 0:
            reverse.append(n % 2)
            n //= 2
        for i in range(len(reverse), 32):
            reverse.append(0)
        
        rev = 0
        for i in range(31, -1, -1):
            rev += reverse[i] * 2 ** (len(reverse) - 1 - i)
        
        return rev