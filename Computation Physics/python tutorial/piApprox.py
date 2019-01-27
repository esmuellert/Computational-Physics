def piApprox(n):
    sum = 0
    for i in range(n):
        
        sum = sum + 4/(2*i+1)*pow(-1,i)
    return sum

a = piApprox(1000)
print(a)


