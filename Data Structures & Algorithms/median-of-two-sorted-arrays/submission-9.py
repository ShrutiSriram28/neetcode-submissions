class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # nums = []
        # k1 = 0
        # k2 = 0

        # if len(nums1) == 0:
        #     if len(nums2) % 2 == 1:
        #         return nums2[len(nums2)//2]
        #     else:
        #         return (nums2[len(nums2)//2] +  nums2[len(nums2)//2 - 1])/2
        # if len(nums2) == 0:
        #     if len(nums1) % 2 == 1:
        #         return nums1[len(nums1)//2]
        #     else:
        #         return (nums1[len(nums1)//2] +  nums1[len(nums1)//2 - 1])/2

        # total = len(nums1) + len(nums2)
        
        # while k1 + k2 <= (total//2) and k1 < len(nums1) and k2 < len(nums2):
        #     if nums1[k1] <= nums2[k2]:
        #         nums.append(nums1[k1])
        #         k1 += 1
        #     else:
        #         nums.append(nums2[k2])
        #         k2 += 1
        # if k1 + k2 <= (total//2) and k1 < len(nums1):
        #     nums.append(nums1[k1])
        #     k1 += 1
        # if k1 + k2 <= (total//2) and k2 < len(nums2):
        #     nums.append(nums2[k2])
        #     k2 += 1
        # print(nums)
        # if total % 2 == 1:
        #     return nums[-1]
        # else:
        #     return (nums[-1] + nums[-2])/2


        # nums = []
        k1 = 0
        k2 = 0

        if len(nums1) == 0:
            if len(nums2) % 2 == 1:
                return nums2[len(nums2)//2]
            else:
                return (nums2[len(nums2)//2] +  nums2[len(nums2)//2 - 1])/2
        if len(nums2) == 0:
            if len(nums1) % 2 == 1:
                return nums1[len(nums1)//2]
            else:
                return (nums1[len(nums1)//2] +  nums1[len(nums1)//2 - 1])/2

        total = len(nums1) + len(nums2)
        
        while k1 + k2 <= (total//2) and k1 < len(nums1) and k2 < len(nums2):
            if nums1[k1] <= nums2[k2]:
                # nums.append(nums1[k1])
                k1 += 1
            else:
                # nums.append(nums2[k2])
                k2 += 1
        if k1 + k2 <= (total//2) and k1 < len(nums1):
            # nums.append(nums1[k1])
            k1 += 1
        if k1 + k2 <= (total//2) and k2 < len(nums2):
            # nums.append(nums2[k2])
            k2 += 1
        # print(nums)
        print(k1, k2)
        if total % 2 == 1:
            if k1 > k2:
                return nums1[k1 - 1]
            elif k2 > k1:
                return nums2[k2 - 1]
            elif k1 == k2:
                if nums1[k1 - 1] > nums2[k2 - 1]:
                    return nums1[k1 - 1]
                else:
                    return nums2[k2 - 1]
        else:
            if k1 - k2 >= 2:
                return (nums1[k1 - 1] + nums1[k1 - 2])/2
            if k2 - k1 >= 2:
                return (nums2[k2 - 1] + nums2[k2 - 2])/2
            else:
                return (nums1[k1 - 1] + nums2[k2 - 1])/2

