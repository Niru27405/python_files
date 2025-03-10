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

n = int(input())
arr = list(map(int, input().split()))

# precompute:
hash = [0] * 13
for i in range(n):
    hash[arr[i]] += 1

q = int(input())
for _ in range(q):
    number = int(input())
    # fetching:
    print(hash[number])

n = str(input())
c = str(input())
cnt = 0
for char in n:
    if char == c:
        cnt += 1
print(cnt)






    
