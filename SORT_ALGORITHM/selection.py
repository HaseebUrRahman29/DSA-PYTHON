#SELECTION SORT
nums=[1,7,8,4,5,6,9,2]
def selection_sort(nums):
    n=len(nums)
    for i in range(0,n):
        min_idx=i
        for j in range(i+1,n):
            if nums[i]>nums[j]:
                min_idx=j
                nums[i],nums[j]=nums[j],nums[i]
    print(nums)

selection_sort(nums)

# DESCENDING ORDER
# nums=[1,7,8,4,5,6,9,2]
# def selection_sort(nums):
#     n=len(nums)
#     for i in range(n-1,0,-1):
#         max_idx=i
#         for j in range(i-1,-1,-1):
#             if nums[i]>nums[j]:
#                 max_idx=j
#                 nums[i],nums[j]=nums[j],nums[i]
#     print(nums)

# selection_sort(nums)