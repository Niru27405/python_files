def f(cnt):
    
    if(cnt == 4):
        return
    print(cnt)
    
    f(cnt +1)
    
n = int(input())
f(0)