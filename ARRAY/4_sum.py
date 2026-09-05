#4SUMPROBLEM
# #brute force
# arr=[1,0,-1,0,-2,2,5,9]
# n=len(arr)
# res=[]
# my_set=set()
# for i in range(0,n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             for l in range(k+1,n):
#                 if arr[i]+arr[j]+arr[k]+arr[l]==0:
#                     temp=[arr[i],arr[j],arr[k],arr[l]]
#                     temp.sort()
#                     my_set.add(tuple(temp))
# print(my_set)

#optimal

from typing import List
class solution:
    def fourSum(self,nums:List[int],target:int) -> List[List[int]]:
        n=len(nums)
        ans=[]
        nums.sort()
        for i in range(n):
            if nums[i]==nums[i-1] and i>0:
                continue
            for j in range(i+1,n):
                if nums[j]==nums[j-1] and j>i+1:
                    continue
                k=j+1
                l=n-1
                while k<l:
                    total=nums[i]+nums[j]+nums[k]+nums[l]
                    if total<target:
                        k+=1
                    elif total>target:
                        l-=1
                    else:
                        ans.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1
                        l-=1
                        while k<l and nums[k]==nums[k-1]:
                            k+=1
                        while l>k and nums[l]==nums[l+1]:
                            l-=1
            return ans