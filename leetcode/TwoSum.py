# Brute Force

n = list(map(int,input().split()))
t = int(input())
for i in range(len(n)):
    for j in range(len(n)):
        if(i==j):
            continue
        if(n[i]+n[j]==t):
            print(i,j)

# Optimal solution

n = list(map(int,input().split()))
t = int(input())
i=0
for i in range(i+1,len(n)):
    for j in range(len(n)):
        if(n[i]+n[j]==t):
            print(i,j)