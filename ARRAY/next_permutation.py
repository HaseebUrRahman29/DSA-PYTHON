#LEETCODE 31 
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        piv = -1

        # Step 1: Find pivot
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                piv = i
                break

        # Step 2: Find element greater than pivot and swap
        if piv != -1:
            for j in range(n-1, piv, -1):
                if nums[j] > nums[piv]:
                    nums[piv], nums[j] = nums[j], nums[piv]
                    break

        # Step 3: Reverse elements after pivot
        i = piv + 1
        j = n - 1

        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1