class Solution:
    def countBits(self, n: int) -> List[int]:
        one = []
        for i in range(n + 1):
            ones = 0
            while i > 0:
                ones += i % 2
                i //= 2
            one.append(ones)
        return one