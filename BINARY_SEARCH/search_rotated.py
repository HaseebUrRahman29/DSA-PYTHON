#SEARCH IN ROTATED SORTED ARRAY(33)
nums=[11,15,20,1,4,5,6,8,9,10]
target=11
n=len(nums)
low=0
high=n-1
while low<=high:
    mid=(low+high)//2
    if target==nums[mid]:
        print(mid)
        break
    if nums[mid]<=nums[high]:
        if nums[mid]<=target<=nums[high]:
            low=mid+1
        else:
            high=mid-1
    else:
        if nums[low]<=target<=nums[mid]:
            high=mid-1
        else:
            low=mid+1
