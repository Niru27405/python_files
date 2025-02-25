def f(cnt):
    
    if(cnt == 4):
        return
    print(cnt)
    
    f(cnt +1)
    
n = int(input())
f(0) 
# print name 5 times using recursion

def f(i,n):
    if(i>n):
        return
    print("raj")
    f(i+1,n)
n = int(input())
f(14,n)

# print linearly from 1-n
def f(i,n):
    if(i>n):
        return
    print(i)
    f(i+1,n)
n = int(input())
f(1,n) 

# print linearly from n-1
def f(i,n):
    if(i<1):
        return
    print(i)
    f(i-1,n)

n = int(input())
f(n,n)

# print linearly from n-1(BackTracking)
def f(i,n):
    if(i<1):
        return
    f(i-1,n)
    print(i)
    

n = int(input())
f(n,n)

# print linearly from 1-n(BackTracking)
def f(i,n):
    if(i>n):
        return
    f(i+1,n)
    print(i)
n = int(input())
f(1,n)

# print sum of first N numbers(parameterized)
def f(i,sum):
    if(i<1):
        print(sum)
        return 
    f(i-1,sum +i)
n = int(input())
f(n,0)

# print sum of first N numbers(functional)
def f (n):
    if(n==0):
        return 0
    return n + f(n-1)
n = int(input())
print(f(n))

# print factorial of N
def f(n):
    if (n==0):
        return 1
    return n*f(n-1)
n = int(input())
print(f(n)) 

# reverse an array (recursion)(double pointer)
def f(arr,l,r):
    if l>=r:
        return
    arr[l],arr[r] = arr[r],arr[l]
    f(arr, l+1, r-1)

arr = list(map(int, input().split()))
f(arr,0,len(arr)-1)
print(arr)

# reverse an array (recursion)(single pointer)
def f(i):
    if(i>=len(a)/2):
        return
    a[i], a[len(a)-i-1]= a[len(a)-i-1] , a[i]
    f(i+1)
a = list(map(int, input().split()))
f(0)
print(a)

# Check if a string is a palindrome
def f(i):
    if(i>=len(n)/2):
        return True
    elif n[i] != n[len(n)-i-1]:
        return False
    return f(i+1)
n = str(input())
if f(0):
    print ("Palindrome")
else:
    print("Not Palindrome")

# Fibonacci Series
def f(n):
    if(n<=1):
        return n
    return f(n-1)+f(n-2)
n = int(input())
f(n)
print(f(n))

# Print all subsequences 
def f(ind,arr,n):
    if(ind >= len(n)):
        print(arr)
        return
    arr.append(n[ind])
    f(ind+1,arr,n)
    arr.pop()
    f(ind+1,arr,n)
n = list(map(int,input().split()))
f(0,[],n)
