#LEETCODE 53
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val=float("-inf")
        total=0
        for i in nums:
            total+=i
            max_val=max(max_val,total)
            if total<0:
                total=0
        return max_val