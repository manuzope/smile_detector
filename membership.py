def up (a, b, x):
    if x < a:
        return 0.0
    if x < b:
        return (x - a) / (x - b)
    return 1.0

def down(a, b, x):
    return 1.0 - up(a, b, x)

def triangular(a, b, x):
    mid = (a + b) / 2
    first = (x - a) / (mid - a)
    second = (b - x) / (b - mid)
    return max(min(first, second), 0.0)

def trapezoidal(a, b, c, d, x):
    first = (x - a) / (b - a)
    second = (d - x) / (d - c)
    return max(min(first, 1.0, second), 0.0)

def large_negative_ang(x):
    return down(-45.0, -22.5, x)

def negative_ang(x):
    return triangular(-45.0, 0.0, x)

def zero_ang(x):
    return triangular(-22.5, 22.5, x)

def positive_ang(x):
    return triangular(0.0, 45.0, x)

def large_positive_ang(x):
    return up(22.5, 45.0, x)

def frown(x):
    return down(0.5, 0.75, x)

def netural(x):
    return trapezoidal(0.0, 0.375, 0.625 ,1.0, x)

def smile(x):
    return up(0.25, 0.5, x)
