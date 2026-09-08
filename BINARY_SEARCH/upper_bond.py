#UPPER BOND
nums=[1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
n=len(nums)
low=0
high=n-1
ub=n
target=1
while low<=high:
    mid=(low+high)//2
    if target<nums[mid]:
        high=mid-1
        ub=mid
    else:
        low=mid+1

print(ub)