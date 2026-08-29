# #REARRANGE ARRAY ELEMENTS BY SIGN(less optimal)
# nums=[5,10,-3,-1,-10,6]
# positive=[]
# negative=[]
# result=[]
# n=len(nums)
# for i in nums:
#     if i>0:
#         positive.append(i)

# for i in nums:
#     if i<0:
#         negative.append(i)


# for i in range(n//2):
#     result.append(positive[i])
#     result.append(negative[i])

# print(result)


#OPTIMAL
nums=[5,10,-3,-1,-10,6]
result=[0]*6
n=len(nums)
pos=0
neg=1
for i in nums:
    if i>0:
        result[pos]=i
        pos+=2
    else:
        result[neg]=i
        neg+=2
print(result)