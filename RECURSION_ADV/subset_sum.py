#SUBSET SUM    
class Solution:
    def solve(self, ind, total, arr, result):
        if ind >= len(arr):
            result.append(total)
            return

        self.solve(ind + 1, total + arr[ind], arr, result)
        self.solve(ind + 1, total, arr, result)

    def subsetSums(self, arr):
        result = []
        self.solve(0, 0, arr, result)
        return result