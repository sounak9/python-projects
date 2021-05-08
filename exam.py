str1=input("enter the string ")
vowels=0
consonent=0
blank=0
for i in str1:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        vowels = vowels +1

        if(i==" "):
            blank=blank+1
    else:
        consonent=consonent+1
print(vowels)
print(consonent)
print(blank)


