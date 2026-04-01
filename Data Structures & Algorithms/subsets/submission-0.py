class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def getBinary(v, d):
            binary = []
            if v == 0:
                binary = [0] * d
            while v > 0:
                binary.append(v % 2)
                v //= 2
            for i in range(d - len(binary)):
                binary.append(0)
            binary.reverse()
            return binary

        superset = []
        for i in range(2 ** len(nums)):
            binary = getBinary(i, len(nums))
            set_ = []
            for i in range(len(binary)):
                if binary[i] == 1:
                    set_.append(nums[i])
            superset.append(set_)

        return superset