def test():
    sumOfSeven = 0
    sumOfNine = 0
    
    for i in range(0,10000,7):
        sumOfSeven = sumOfSeven + i

    for i in range(0,10000,9):
        sumOfNine = sumOfNine + i

    total = sumOfNine + sumOfSeven
    print(total)

test()