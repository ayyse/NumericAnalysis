from decimal import getcontext, Decimal

getcontext().prec = 3

def forwardDifference(f, x, h):
    func = ((-1) * f(x + (2 * h))) + (4 * f(x + h)) - (3 * f(x)) / (2 * h)
    return print(f"Forward difference not calculate, x = {x + 2 * h} not given")


def backwardDifference(f, x, h):
    return round((3 * f(x)) - (4 * f(x - h)) + f(x - 2 * h) / (2 * h), 2)


def centralDifference(f, x, h):
    return f(x + h) - f(x - h) / (2 * h)


def secondForward(f, x, h):
    func = ((2 * f(x)) - (5 * f(x + h)) + (4 * f(x + (2 * h))) - f(x + (3 * h))) / (h * h)
    error = print(f"Forward second difference not calculate, x = {x + 2 * h} and x = {Decimal(x) + 3 * Decimal(h)} not given")
    return error


def secondBackward(f, x, h):
    func = ((2 * f(x)) - (5 * f(x - h)) + (4 * f(x - (2 * h))) - f(x - (3 * h))) / (h * h)
    error = print(f"Backward second difference not calculate, x = {x - 3 * h} not given")
    return error


def secondCentral(f, x, h):
    return f(x - h) - 2 * f(x) + f(x + h) / (h * h)

def myFunc(x):
    if x == 2.38:
        x = 0.86710
    if x + h:
        y = 0.87129

    if x - h:
        y = 0.86289
    if x - 2 * h:
        y = 0.85866
    return y

x = 2.38
h = 0.01
# print(x+h) burada x+h ı tam sonuç vermediği için işlemler hatalı geliyor


print("Forward difference =", forwardDifference(myFunc, x, h))
print("Backward difference =", backwardDifference(myFunc, x, h))
print("Central difference =", centralDifference(myFunc, x, h))

print("Forward second difference=", secondForward(myFunc, x, h))
print("Backward second difference =", secondBackward(myFunc, x, h))
print("Central socond difference =", secondCentral(myFunc, x, h))
