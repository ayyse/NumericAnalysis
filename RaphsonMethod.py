# NEWTON RAPHSON METHOD
x = -1

for i in range(1, 100):
    y = (3 * x ** 3) + (x ** 2) - x - 5
    dy = (9 * x ** 2) + 2 * x - 1

    xn = x - (y / dy)
    if abs(xn - x) < 0.00000001: break
    x = xn
    print("The root is %f at %d iterations" % (xn, i))

print("9. and 10. iterations are same.Root is %f" % xn)


