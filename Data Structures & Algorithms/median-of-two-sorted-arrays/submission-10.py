class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        
        total = len(A) + len(B)
        half = (len(A) + len(B))//2
        l, r = 0, len(A) - 1
        
        while True:
            i = (l + r)//2      # i is the index for A
            j = half - i - 2    # j is the index for B, so subract 1 for each of i and j

            ALeft = A[i] if i >= 0 else float("-inf")
            ARight = A[i + 1] if (i + 1) < len(A) else float("inf")
            BLeft = B[j] if j >= 0 else float("-inf")
            BRight = B[j + 1] if (j + 1) < len(B) else float("inf")
            
            if ALeft <= BRight and BLeft <= ARight:
                if total % 2 != 0:
                    return min(ARight, BRight)
                else:
                    return (max(ALeft, BLeft) + min(ARight, BRight))/2
            elif ALeft > BRight:
                r = i - 1
            else:
                l = i + 1
