#RECURSION USING PARAMETERS
def num(x,n):
    if n==0:
        return
    print(x)
    num(x,n-1)

num(15,4)