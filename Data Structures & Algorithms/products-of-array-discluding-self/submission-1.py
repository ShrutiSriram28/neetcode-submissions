class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        prod_arr = []
        if 0 not in nums:
            for i in nums:
                prod *= i
            prod_arr = [prod//i for i in nums]
        else:
            ind = 0
            flag = 0
            prod_arr = [0 for i in range(len(nums))]
            for i in range(len(nums)):
                if flag == 0 and nums[i] == 0:
                    ind = i
                    flag = 1
                    continue
                prod *= nums[i]
            if prod != 0:
                prod_arr[ind] = prod
        
        return prod_arr
                


        

