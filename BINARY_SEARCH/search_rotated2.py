#SEARCH IN ROTATED ARRAY 2(81)
nums=[10,11,11,12,12,13,13,13,1,2,3,4]
n=len(nums)
low=0
high=n-1
target=12
while low<=high:
    mid=(low+high)//2
    if nums[mid]==target:
        print(True)
        break
    if nums[low]==nums[mid]==nums[high]:
        low+=1
        high-=1
        continue
    if nums[mid]>=nums[low]:
        if nums[low]<=target<=nums[mid]:
            high=mid-1
        else:
            low=mid+1
    else:
        if nums[mid]<=target<=nums[mid]:
            low=mid+1
        else:
            high=mid+1
else:
    print(False)