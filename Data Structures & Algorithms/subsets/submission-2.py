class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        superset = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                # Appending subset.copy() is necessary because when we append subset, it is a pass by reference. 
                # Any changes to subset would be reflected in the list that's appended to superset.
                
                superset.append(subset.copy())
                return
        
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)

        dfs(0)
        return superset



# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         def getBinary(v, d):
#             binary = []
#             if v == 0:
#                 binary = [0] * d
#             while v > 0:
#                 binary.append(v % 2)
#                 v //= 2
#             for i in range(d - len(binary)):
#                 binary.append(0)
#             binary.reverse()
#             return binary

#         superset = []
#         for i in range(2 ** len(nums)):
#             binary = getBinary(i, len(nums))
#             set_ = []
#             for i in range(len(binary)):
#                 if binary[i] == 1:
#                     set_.append(nums[i])
#             superset.append(set_)

#         return superset