print("=========== FIRST PROGRAM ==========")

X = lambda a : a+10
print(X(10))


print("========== SECOND PROOGRAM =========")

X = lambda x,y : x*y
print(X(100,200))

print("============ ******** ============")

Y = lambda a,b,c : a*b+c
print(Y(10,20,30))

print("============= ****** =============")

def my (A):
    return lambda t : t*A

X = my(10)
print(X(20))
print(X(30))


