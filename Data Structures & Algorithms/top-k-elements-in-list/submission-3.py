class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq = {}
        # freq_ele = {}
        # kfreq = []
        
        # for i in range(len(nums) + 1):
        #     freq_ele[i] = []
        # for i in range(len(nums)):
        #     freq[nums[i]] = 1 + freq.get(nums[i], 0)
        # for i,v in freq.items():
        #     freq_ele[v].append(i)
        # for i in range(len(nums), -1, -1):
        #     if (len(freq_ele[i])) > 0:
        #         for ele in freq_ele[i]:
        #             kfreq.append(ele)
        
        # return kfreq[:k]


        freq = [[] for i in range(len(nums) + 1)]
        count = {}
        kfreq = []

        for i in nums:
            count[i] = 1 + count.get(i, 0)
        
        for key, val in count.items():
            freq[val].append(key)
        
        for i in range(len(nums), -1, -1):
            kfreq.extend(freq[i])
        
        return kfreq[:k]