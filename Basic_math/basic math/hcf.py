n = int(input())
v = int(input())
for i in range(1,n+1):
    if(n%i==0)and(v%i==0):
        gcd = i
print(gcd)

