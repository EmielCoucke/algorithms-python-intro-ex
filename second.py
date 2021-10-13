def Lucas(n):
    if n==0:
        return 2
    if n==1:
        return 1
    return Lucas(n-1) + Lucas(n-2)

for i in range(0,32):
    print(Lucas(i))