# selection sort

n = list(map(int,input().split()))

for i in range(len(n)-1):
    mins = i
    for j in range(i+1,len(n)):
        if n[j]<n[mins]:
            mins = j
    n[i],n[mins] = n[mins],n[i]
        
print(n)
