# #BruteForce

# def subarray(arr,k):
#     n = len(arr)
#     maxlen = 0
    
#     for i in range(n):
#         sum = 0

#         for j in range(i,n):
#             sum += arr[j]
#             if sum <= k:
#                 maxlen = max(maxlen,j-i+1)
            
#     return maxlen
# arr = list(map(int,input().split()))
# k = int(input())
# res = subarray(arr,k)
# print(res)


# # optimized brute force

# def subarray(arr,k):
#     n = len(arr)
#     maxlen = 0
    
#     for i in range(n):
#         sum = 0

#         for j in range(i,n):
#             sum += arr[j]
#             if sum <= k:
#                 maxlen = max(maxlen,j-i+1)
#             elif sum > k :
#                 break
#     return maxlen
# arr = list(map(int,input().split()))
# k = int(input())
# res = subarray(arr,k)
# print(res)


# Better Approach with sliding window and two pointer

def subarray(arr,k):
    n = len(arr)
    l = r = sum = maxlen = 0
    while r < n :
        sum += arr[r]
        while sum > k:
            sum -= arr[l]
            l += 1
        if sum < k:
            maxlen = max(maxlen,r-l+1)
        r+=1
    return maxlen
arr = list(map(int,input().split()))
k = int(input())
print(subarray(arr,k))

# Better Approach with sliding window and two pointer (optimal)

def subarray(arr,k):
    n = len(arr)
    l = r = sum = maxlen = 0
    while r < n :
        sum += arr[r]
        if sum > k:
            sum -= arr[l]
            l += 1
        if sum < k:
            maxlen = max(maxlen,r-l+1)
        r+=1
    return maxlen
arr = list(map(int,input().split()))
k = int(input())
print(subarray(arr,k))