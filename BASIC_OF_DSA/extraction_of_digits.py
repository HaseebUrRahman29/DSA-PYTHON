#Extraction of digit
num=5873
while num>0:
    lastdigit=num%10
    print(lastdigit)
    num=num//10