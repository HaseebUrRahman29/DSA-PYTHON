#RIGHT ROTATE AN ARRAY BY K PLACE(brute force)
# nums=[5,-2,3,9,0,6,10,7]
# k=3
# n=len(nums)
# rotation=k%n
# for _ in range(0,rotation):
#     e=nums.pop()
#     nums.insert(0,e)
# print(nums)

# #better approach
# nums=[5,-2,3,9,0,6,10,7]
# n=len(nums)
# k=5
# k=k%n
# nums[:]=nums[n-k:]+nums[:n-k]
# print(nums)

#optimal way
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