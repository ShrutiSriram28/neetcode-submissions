class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        a = arr[0]
        an = arr[len(arr) - 1]
        n = len(arr)
        d = (an - a)//n

        l = 0
        r = len(arr) - 1

        while l <= r:
            mid = (l + r)//2
            if arr[mid] == a + mid * d:
                l = mid + 1
            else:
                r = mid - 1
        
        return arr[r] + d