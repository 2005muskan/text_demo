A = [10,20,30,40,50,60,70,80,90,100]

def marks(B):
    if B>=60:
        return True
    else:
        return False
    
result = filter(marks,A)
for i in result:
    print(i)
print(type(result))

print("++++++++++++++++++++++++++++++++")

B = [1,2,3,4,5,6,7,8,9,10]

def number(A):
    if A>=8:
        print("Hello")
    else:
        print("Thank you")

num = filter(number,B)
for i in num:
    print(i)
print(type(num))

print("========== stop ============")


