# Brute Force

n = list(map(int,input().split()))
n.sort()
unique = set()
for i in range(len(n)):
    for j in range(i+1,len(n)):
        for k in range(j+1,len(n)):
            if n[i]+n[j]+n[k]==0:
                unique.add((n[i],n[j],n[k]))
for t in unique:
    print(t)

# Better Approach

n = list(map(int,input().split()))
n.sort()
a = []
for i in range(len(n)):
    if(i>0 and n[i]==n[i-1]):
        continue
    j = i+1
    k = len(n)-1
    while(j<k):
        sum = n[i]+n[j]+n[k]
        if (sum<0):
            j += 1
        elif (sum >0):
            k -= 1
        else:
            a.append((n[i],n[j],n[k]))
            j += 1
            k -= 1
            while(j<k and n[j]==n[j-1]):
                j += 1

            while(j<k and n[k]==n[k+1]):
                k -= 1
print(a)

