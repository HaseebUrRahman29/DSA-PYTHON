#CHECK IF A NUMBER IS ARMSTRONG OR NOT
n=153
num=n
no_of_digit=len(str(n))
total=0
while num>0:
    lastdigit=num%10
    total+=lastdigit**no_of_digit
    num=num//10
print(n==total)