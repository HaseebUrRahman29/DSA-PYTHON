#REVERSE AN ARRAY USING RECURSION
num=[5,7,3,2,6,1,5,9]
reverse_num=[]
l=0
r=len(num)-1
def fun(num,l,r):
    if l>=r:
        print(num)
        return
    num[l],num[r]=num[r],num[l]
    fun(num,l+1,r-1)
fun(num,l,r)