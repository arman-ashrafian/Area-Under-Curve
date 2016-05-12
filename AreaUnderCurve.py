# AP Calc
# Finds definite integral (area under a curve)

# Arman Ashrafian

print("Use Python syntax")
print("Ctrl-C to end script\n")

def main() :

    global equation
    equation = input("f(x) = ")

    leftEnd = int(input("lower bound: "))
    rightEnd = int(input("upper bound: "))
    num = int(input("Number of rectangles or trapezoids: "))
    dx = (rightEnd - leftEnd)/float(num)
    
    print("Change of x = ", dx)
    print("Leftend sum = ", LeftEndSum(num, leftEnd, dx))
    print("Rightend sum = ", RightEndSum(num, leftEnd, dx))
    

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

main()
