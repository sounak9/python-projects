str=input("enter a string : ")
upper = 0
lower = 0
for i in range(len(str)):
    if(str[i]>='a' and str[i]<='z'):
        lower+=1
    elif(str[i]>='A' and str[i]<='z'):
        upper+=1
print('lower case letters= ',lower)
print('upper case letters= ',upper)
