#CHARACTER HASHING
s="azyxyyzaaaa"
q=["d","a","y","x"]
new_dict={}

for i in s:
    if i in new_dict:
        new_dict[i]+=1
    else:
        new_dict[i]=1

for i in q:
    print(i,":",new_dict.get(i,0))