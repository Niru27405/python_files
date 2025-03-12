# 74. Search a 2D Matrix
import json
def f(matrix,target):
    m = len(matrix)
    n = len(matrix[0])
    t = m*n
    l = 0
    r = t-1
    
    while l<=r:
        M = (l+r)//2
        i = M//n
        j = M%n

        num = matrix[i][j]
        if target == num :
            return True
        elif target < num:
            r = M-1
        else:
            l = M+1
    return False

                



matrix = json.loads(input())
target = int(input())

print(f(matrix,target))