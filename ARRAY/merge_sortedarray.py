#MERGE TWO SORTED ARRAY
num1=[1,1,1,2,4,6,7]
num2=[1,2,3,6,7,8,9,10]
n=len(num1)
m=len(num2)
i,j=0,0
result=[]
while i<n and j<m:
    if num1[i]<=num2[j]:
        if len(result)==0 or num1[i]!=result[-1]:
            result.append(num1[i])
        i+=1
    else:
        if len(result)==0 or num2[j]!=result[-1]:
            result.append(num2[j])
        j+=1
while i<n:
        if len(result)==0 or num1[i]!=result[-1]:
            result.append(num1[i])
        i+=1
while j<m:
        if len(result)==0 or num2[j]!=result[-1]:
            result.append(num2[j])
        j+=1
print(result)