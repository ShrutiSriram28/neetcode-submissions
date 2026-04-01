class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = []
        kfreq = []
        for i in range(len(nums)):
            freq.append([])

        count_no = {}
        for no in nums:
            count_no[no] = count_no.get(no, 0) + 1

        for key, value in count_no.items():
            freq[value - 1].append(key)

        for i in range(len(freq) - 1, -1, -1):
            for j in range(len(freq[i])):
                kfreq.append(freq[i][j])

        return kfreq[:k]
