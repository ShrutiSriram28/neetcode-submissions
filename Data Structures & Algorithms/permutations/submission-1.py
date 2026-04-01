class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])
        res = []
        for p in perms: 
            for i in range(len(p) + 1):
                perm = p.copy()
                perm.insert(i, nums[0])
                res.append(perm)

        return res