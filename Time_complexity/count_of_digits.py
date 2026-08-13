#Count of digit
num=5873
count=0
while num>0:
    lastdigit=num%10
    count+=1
    num=num//10
print(count)