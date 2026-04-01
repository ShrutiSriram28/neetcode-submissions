class Solution:
    def myPow(self, x: float, n: int) -> float:
        p = 1

        if n > 0:
            for i in range(1, n + 1):
                p *= x
        else:
            for i in range(n, 0):
                p /= x

        return p