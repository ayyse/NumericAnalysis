(x0, y0) = (-2, 8)
(x1, y1) = (0, 4)
(x2, y2) = (1, 2)
(x3, y3) = (3, -2)

a1 = y0

step1 = (y1 - y0) / (x1 - x0)
step2 = (y2 - y1) / (x2 - x1)
step3 = (y3 - y2) / (x3- x2)

a2 = step1

step4 = (step2 - step1) / (x2 - x0)

a3 = step4

step5 = (step3 - step2) / (x3 - x1)

print(f"p = {a1} + ({a2} * (x - {x0})) + ({a3} * (x - {x0}) * (x - {x1})) ")