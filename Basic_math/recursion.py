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
