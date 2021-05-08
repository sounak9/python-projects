def number(n):
    S = 0
    for i in range(0, n+1):
        S += i * i - (i - 1) * (i - 1)
     
    return S
 
# Driver Code
n = 500
print("The sum of n term is: ",number(n), sep = "")