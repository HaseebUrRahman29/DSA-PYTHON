#COUNT THE OCCURENCES OF A NUMBER(binary search)
nums=[1,2,3,3,3,3,3,5,6,8,9,9,10]
n=len(nums)
count=0
low=0
high=n-1
target=3
first=-1
last=-1
while low<=high:
    mid=(low+high)//2
    if nums[mid]>=target:
        if nums[mid]==target:
            first=mid
        high=mid-1
    else:
        low=mid+1
low=0
high=n-1
while low<=high:
    mid=(low+high)//2
    if nums[mid]<=target:
        if nums[mid]==target:
            last=mid
        low=mid+1
    else:
        high=mid-1

if first==-1:
    count=0
else:
    count=last-(first-1)
print(count)

#TC:O(logn)
#Sc:O(1)