class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
            if len(hashmap) == 3:
                for k in list(hashmap.keys()):
                    hashmap[k] -= 1
                    if hashmap[k] == 0:
                        del hashmap[k]
        
        print(hashmap)
        res = []
        for k, v in hashmap.items():
            if nums.count(k) > len(nums)//3:
                res.append(k)

        return res