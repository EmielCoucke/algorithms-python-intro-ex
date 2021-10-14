import math

def Line(x1,y1,x2,y2):
    x = abs(x1 - x2)
    y = abs(y1 - y2)
    Pythagoras = math.sqrt(x*x + y*y)

    return Pythagoras

print(Line(4,7,8,5))
