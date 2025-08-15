def constantwindow(arr,k):
    n = len(arr)
    if k > n:
        return None
    l,r = 0,k-1
    sum1 = sum(arr[l:r+1])
    maxsum = sum1

    while r < n - 1:
        sum1 -= arr[l]
        l += 1
        r += 1
        sum1 += arr[r]
        maxsum = max(maxsum,sum1)
    return maxsum


arr = list(map(int,input().split()))
k = int(input())
res = constantwindow(arr,k)
print(res)