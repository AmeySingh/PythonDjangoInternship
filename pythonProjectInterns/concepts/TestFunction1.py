#varibale number of arguments
#
def addition(a,b,*args):
    result = a+b

    for i in args:
        result = result + i

    return result


print(addition(10,25,1,2,3,4,5))
print(addition(11,2,3,4,6))

