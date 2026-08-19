#PRINT 1 TO N USING RECURSION
#TAIL RECURSION WHERE RECURSION IS AT LAST
def num(first,last):
    if first>last:
        return
    print(first)
    num(first+1,last)

num(1,10)

# #HEAD RECURSION WHERE RECURSION IS BEFORE WORK AND IT RESULT IN OPPOSITE MANNER
# def num(first,last):
#     if first>last:
#         return
#     num(first+1,last)
#     print(first)

# num(1,10)