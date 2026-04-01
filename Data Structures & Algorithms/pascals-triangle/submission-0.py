class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]]
        for i in range(numRows - 1):
            temp = [0] + pascal[-1] + [0]
            row = []
            for j in range(len(temp) - 1):
                row.append(temp[j] + temp[j + 1])
            pascal.append(row)
        return pascal