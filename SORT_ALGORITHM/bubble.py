#BUBBLE SORT
nums=[5,8,1,6,9,2,4]
def bubble_sort(nums):
    n=len(nums)
    for i in range(n-2,-1,-1):
        swap=False
        for j in range(0,i+1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                swap=True
        if(swap==False):
            break

    print(nums)

bubble_sort(nums)