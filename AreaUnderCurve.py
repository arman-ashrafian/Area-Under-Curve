# AP Calc
# Finds definite integral (area under a curve)

# Arman Ashrafian

import math

print("Use Python syntax")
print("Ctrl-C to end script\n")

def main() :

    global equation
    equation = input("f(x) = ")

    leftEnd = int(input("lower bound: "))
    rightEnd = int(input("upper bound: "))
    num = int(input("Number of rectangles or trapezoids: "))
    dx = (rightEnd - leftEnd)/float(num)

    print()
    print("Change of x = ", dx)
    print("Leftend sum = ", LeftEndSum(num, leftEnd, dx))
    print("Rightend sum = ", RightEndSum(num, leftEnd, dx))
    print("Trapezaid sum = ", Trapezoid(num, leftEnd, dx))
    print("Midpoint sum = ", Midpoint(num, leftEnd, dx))
    print("Simpson sum = ", Simpson(num, leftEnd, dx))
    print()

    if(isIncreasing(num, leftEnd, dx)):
        print("Function is increasing\n")
    elif(isIncreasing(num, leftEnd, dx) == False):
        print("Function is decreasing\n")
    else:
        print()

def LeftEndSum(num, leftEnd, dx) :
    sum = 0.0
    for i in range(num):
        x = leftEnd + (i * dx)
        y = eval(equation)
        sum += y*dx
    return sum

def RightEndSum(num, leftEnd, dx) :
    sum = 0.0
    for i in range(num):
        x = leftEnd + ((i+1) * dx)
        y = eval(equation)
        sum += y*dx
    return sum

def Trapezoid(num, leftEnd, dx) :
    sum = .5 * (RightEndSum(num, leftEnd, dx) + LeftEndSum(num, leftEnd, dx))
    return sum

def Midpoint(num, leftEnd, dx) :
    sum = 0.0
    for i in range(num) :
        x = leftEnd + (dx/2) + (i*dx)
        y = eval(equation)
        sum += y*dx
    return sum

def Simpson(num, leftEnd, dx) :
    sum = ((2/3)*Midpoint(num, leftEnd, dx)) + ((1/3)*Trapezoid(num, leftEnd, dx))
    return sum

def isIncreasing(num, leftEnd, dx):
    if(RightEndSum(num, leftEnd, dx) > LeftEndSum(num, leftEnd, dx)):
        return True
    elif(RightEndSum(num, leftEnd, dx) == LeftEndSum(num, leftEnd, dx)):
        return None
    else:
        return False

try:
    while(True):
        main()
except KeyboardInterrupt:
    print("Script Ended")
