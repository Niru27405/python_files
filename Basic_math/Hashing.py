# given an array and asked to count no of times particular no is repeated
# Brute force without hashing
def f(num,n):
    cnt = 0
    for i in range(len(n)):
        if(n[i]==num):
            cnt += 1
    return cnt
n = list(map(int,input().split()))
num = int(input())
d =f(num,n)
print(d)

# Hashing
from collections import Counter
n = int(input())
f = Counter(n)
num = int(input())
print(f[num])




    
