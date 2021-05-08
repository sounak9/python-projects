a=int(input("enter the value"))
b=int(input("enter the value"))
c=int(input("enter the value"))
if a>b and a>c :
    l=a
elif b>a and b>c:
    l=b
else:
    l=c
print("the largest value is ",l)