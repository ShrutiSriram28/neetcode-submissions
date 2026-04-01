class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prod = 1
        # prod_arr = []
        # if 0 not in nums:
        #     for i in nums:
        #         prod *= i
        #     prod_arr = [prod//i for i in nums]
        # else:
        #     ind = 0
        #     flag = 0
        #     prod_arr = [0 for i in range(len(nums))]
        #     for i in range(len(nums)):
        #         if flag == 0 and nums[i] == 0:
        #             ind = i
        #             flag = 1
        #             continue
        #         prod *= nums[i]
        #     if prod != 0:
        #         prod_arr[ind] = prod
        
        # return prod_arr
                
        prefix = [1 for i in range(len(nums))]
        postfix = [1 for i in range(len(nums))]
        prod = [1 for i in range(len(nums))]
        
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
            
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]

        for i in range(len(nums)):
            prod[i] = prefix[i] * postfix[i]

        return prod

# [1 2 4 6]
# [1 1 2 8]
# [48 24 6 1]
        

