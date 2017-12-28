import os, math


def add(a, b):
    os.system('clear')
    print "Adding %d and %d" % (a, b)
    return a + b

def rad(a):
    os.system('clear')
    print "Calculating radius..."
    return float(math.pow(a, 2) * math.pi)


print """
    What do you want to do?
    1. Add two numbers
    2. Calulate area of a circle?

    Choose 1 or 2 and press Enter
    """
answ = int(raw_input(">>>"))

if answ == 1:
    num1 = int(raw_input("Enter frst No#:"))
    num2 = int(raw_input("Enter scnd No#:"))
    sum1 = add(num1, num2)
    print "The sum of the two numbers is %.03d." % sum1
else:
    rad1 = float(raw_input("Enter cm Radius of Circle:"))
    area = rad(rad1)
    print "The area of the circle is %.4f cm2." % area
