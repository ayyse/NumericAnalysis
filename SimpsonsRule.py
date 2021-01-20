a = 0
b = 1
n = int(input("Please press 2, 4 or 6"))
print("You pressed:", n)
h = float((b - a) / n)

def func(x):
    return x * x

if n == 2:
    def twoPanels(f, a, b, h):
        return (h / 3) * (f(a) + (4 * f((a + b) / 2)) + f(b))
    print(twoPanels(func, a, b, h))

if n == 4:
    def fourPanels(f, a, b, h):
        return (h / 3) * (f(a) + (4 * f((a + b) / 4)) + (2 * f((a + b) / 2)) + (4 * f((3 * (a + b)) / 4)) + f(b))
    print(fourPanels(func, a, b, h))

if n == 6:
    def sixPanels(f, a, b, h):
        return (h / 3) * (f(a) + (4 * f(1 / 6)) + (2 * f(1 / 3)) + (4 * f(1 / 2)) + (2 * f(2 / 3)) + (4 * f(5 / 6)) + f(b))
    print(sixPanels(func, a, b, h))




