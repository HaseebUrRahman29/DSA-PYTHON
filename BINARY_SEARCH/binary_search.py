#BINARY SEARCH
nums=[2,4,6,7,9,11,18,19]
n=len(nums)
low=0
high=n-1
target=6
if target in nums:
    while low<=high:
        mid=(low+high)//2
        if target==nums[mid]:
            print(mid)
            break
        elif target<nums[mid]:
            high=mid-1
        else:
            low=mid+1
else:
    print(-1)

#TC:log2(n)
#Sc:0(1)