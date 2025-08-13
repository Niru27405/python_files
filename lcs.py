def lcs (str1,str2):
    m = len(str1)
    n = len(str2)
    maxl = 0
    dp = [[0]*(n+1)for _ in range (m+1)]
    for i in range (1,m+1):
        for j in range (1,n+1):
            
            if (str1[i-1] == str2[j-1]):
                dp[i][j] = dp[i-1][j-1]+1 
                if maxl < dp[i][j]:
                    maxl = dp [i][j]
            else:
                dp[i][j] = 0
    return maxl
str1 = str(input())
str2 = str(input())
print(lcs(str1,str2))
                