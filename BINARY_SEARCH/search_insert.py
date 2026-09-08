#SEARCH INSERT POSITION(35)
nums=[1,3,4,5,8,9,14,15,19,20,21]
target=5
n=len(nums)
low=0
high=n-1
lb=n
while low<=high:
    mid=(low+high)//2
    if nums[mid]>=target:
        lb=mid
        high=mid-1
    else:
        low=mid+1
print(lb)

#TC:log2(n) where n number of elements in list
#Sc=O(1)
