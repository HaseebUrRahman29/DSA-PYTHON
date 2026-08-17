#HASHING
#FINDING ELEMENTS OF M IN N
n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]
new_dict={}
for i in n:
    if(i in new_dict):
        new_dict[i]+=1
    else:
        new_dict[i]=1

for i in m:
    print(i,":",new_dict.get(i,0))