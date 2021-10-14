# current = 1
# previous = 2
# sum = 2

# def luc(n):
#     if n == 0:
#         return 2
#     elif n == 1:
#         return 1
#     else:
#         return luc(n-1) + luc(n -2)
def lucas(n):
    if n==0:
        return 2
    if n==1:
        return 1
    return lucas(n-1) + lucas(n-2)

for i in range(0,32):
    print(lucas(i))