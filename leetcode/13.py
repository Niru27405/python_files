def f(n):
    roman = {"I":1 , "V":5, "X":10 , "L":50 , "C":100 , "D":500 , "M":1000}
    res = 0
    for i in range(len(n)):
        if i+1 < len(n) and roman[n[i]]<roman[n[i+1]]:
            res -= roman[n[i]]
        else:
            res += roman[n[i]]
    return res
 


n = str(input())
print(f(n))
