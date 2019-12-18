# Generating Fibonacci Series by Python

a = [1, 1]
n = 1

while n<10 :
    a.append(a[n-1] + a[n])
    n += 1

print(a)
