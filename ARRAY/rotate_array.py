nums=[5,-2,3,9,0,6,10,7]
n=len(nums)
k=5
k=k%n
def reverse_list(nums,left,right):
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1

reverse_list(nums,n-k,n-1)
reverse_list(nums,0,n-k-1)
reverse_list(nums,0,n-1)
print(nums)

#TC=O(n)
#SC=O(1)