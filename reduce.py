from functools import reduce 

def myfunc(a,b):
    return a+b

val = [1,2,3,4,5]
add = reduce(myfunc,val)
print("Addition =",add)

print("=============================")

from functools import reduce
num = [10,20,30,40,50]
max = reduce(lambda  a,b : a if a>b else b,num)
print("Max = ",max)