#CONTAINS DUPLICATE
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        answer=False
        n=len(nums)
        hashset=set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False