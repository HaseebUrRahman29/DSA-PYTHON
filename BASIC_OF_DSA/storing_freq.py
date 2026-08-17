#STORING FREQUENCY OF A NUMBER IN DICTIONARY
num=[5,6,7,7,1,9,111,1,1,5,1,1]
new_dict={}
for i in num:
    if(i in new_dict):
        new_dict[i]+=1
    else:
        new_dict[i]=1
print(new_dict)