#PRINT ALL FACTORS OF A GIVEN NUMBER(BRUTE FORCE)
n=20
num=20
result=[]
for i in range(1,num+1):
    if(num%i==0):
        result.append(i)
print(result)

#PRINT ALL FACTORS OF A GIVEN NUMBER(BETTER WAY)
# n=20
# num=20
# result=[]
# for i in range(1,num//2):
#     if(num%i==0):
#         result.append(i)
# result.append(num)
# print(result)

# #PRINT ALL FACTORS OF A GIVEN NUMBER(OPTIMAL WAY)
# import math
# n=36
# num=n
# result=[]
# for i in range(1,int(math.sqrt(num))+1):
#     if num%i==0:
#         result.append(i)
#         if (num//i)!=i:
#             result.append(num//i)
# print(result)