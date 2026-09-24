def convert2binary(num:int):
    result=""
    while num>0:
        if num%2==1:
            result+="1"
        else:
            result+="0"
    result=result[::-1]
    return result


def convert2decimal(x:str):
    decimal_number=0
    power=0
    indx=len(x)-1
    while indx>=0:
        num=int(x[indx])*(2**power)
        decimal_number+=num
        indx-=1
        power+=1
    return decimal_number