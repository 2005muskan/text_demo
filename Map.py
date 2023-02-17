def num(a):
    return a + 30

list1 = [5,4,3,2,1]

X = map(num,list1)
print(list(X))

print("+++++++++++++++++++++++++")

def my(y):
    return y * 2
even = [10,20,30,40,50]

M = map(my,even)
print(tuple(M))


