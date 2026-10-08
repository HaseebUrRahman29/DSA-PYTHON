#COMBINATION SUM 3    
class Solution(object):
    def solve(self, last, total, subset, k, n, result):
        if total == n and len(subset) == k:
            result.append(list(subset))
            return

        if total > n or len(subset) > k:
            return

        for i in range(last, 10):
            total_sum = total + i
            subset.append(i)
            self.solve(i + 1, total_sum, subset, k, n, result)
            subset.pop()

    def combinationSum3(self, k, n):
        result = []
        self.solve(1, 0, [], k, n, result)
        return result