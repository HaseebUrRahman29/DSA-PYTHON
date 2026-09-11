#FIND MINIMUM IN ROTATED SORTED ARRAY(153)
nums=[4,5,6,7,0,1,2]
n=len(nums)
low=0
high=n-1
minimum=float("inf")
while low<=high:
    mid=(low+high)//2
    if nums[mid]<=nums[high]:
        minimum=min(minimum,nums[mid])
        high=mid-1
    else:
        minimum=min(minimum,nums[low])
        low=mid+1
print(minimum)