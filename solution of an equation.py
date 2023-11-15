#!/usr/bin/python3
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = (b**2) - 4*a*c
if d < 0 :
    print("The equation has no solutions.")
elif d == 0 :
    x = - b / (2 * a)
    print("The equation has one solution: x =",round(x, 3))
else :
    x1 = (- b - d**0.5) / (2 * a)
    x2 = (- b + d**0.5) / (2 * a)
    print("The solutions of the equation are: x1 =", round(x1, 3), "and x2 =", round(x2, 3))