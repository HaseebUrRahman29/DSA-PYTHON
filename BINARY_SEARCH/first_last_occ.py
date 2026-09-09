#FIRST AND LAST OCCURENCE
nums=[1,2,3,3,3,3,3,5,6,8,9,9,10]
n=len(nums)
target=3
low=0
high=n-1
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

print(first)
print(last)