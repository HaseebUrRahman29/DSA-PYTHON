#CHECK IF A NUMBER IS PALINDROME OR NOT
n=1234
num=n
result=0
while num>0:
    lastdigit=num%10
    result=(result*10)+lastdigit
    num=num//10
if(result==n):
    print("The number is palindrome.")
else:
    print("The number is not a palindrome.")