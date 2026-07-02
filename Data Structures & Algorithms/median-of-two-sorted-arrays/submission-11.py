class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        total = len(nums1) + len(nums2)
        l1 = 0
        r1 = len(nums1) - 1
        half = total // 2

        while True:
            mid1 = (l1 + r1)//2
            mid2 = half - (mid1 + 1) - 1

            left1 = nums1[mid1] if mid1 >= 0 else float("-inf")
            right1 = nums1[mid1 + 1] if mid1 + 1 < len(nums1) else float("inf")
            left2 = nums2[mid2] if mid2 >= 0 else float("-inf")
            right2 = nums2[mid2 + 1] if mid2 + 1 < len(nums2) else float("inf")

            if left1 <= right2 and left2 <= right1:
                if total % 2 == 1:
                    return min(right1, right2)
                return (max(left1, left2) + min(right1, right2)) / 2
            
            elif left1 > right2:
                r1 = mid1 - 1
            
            else:
                l1 = mid1 + 1