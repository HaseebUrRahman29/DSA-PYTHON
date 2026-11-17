#LEETCODE 540  
class Solution(object):
    def singleNonDuplicate(self, nums):
        st = 0
        end = len(nums) - 1

        while st < end:
            mid = (st + end) // 2

            # Make mid even to compare pairs correctly
            if mid % 2 == 1:
                mid -= 1

            # Pair is correct, single element is on the right
            if nums[mid] == nums[mid + 1]:
                st = mid + 2

            # Pair is broken, single element is on the left
            else:
                end = mid

        # st and end meet at the single element
        return nums[st]

# TC: O(log n)
# SC: O(1)