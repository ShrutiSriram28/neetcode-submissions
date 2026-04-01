class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if target - numbers[i] == numbers[i] and numbers[i + 1] == numbers[i]:
                return [i + 1, i + 2]
            elif target - numbers[i] in numbers:
                return [i + 1, numbers.index(target - numbers[i]) + 1]
        return []