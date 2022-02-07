''' Полотнянко вариант17'''

def funct(x):
    return(x**3 + 5*x + 11)

def pohidna(x):
    return(3*x**2 + 5)

def second_pohidna(x):
    return(6*x)

def chord(a, b, eps):
    if funct(a) * funct(b)>0:
        return 0, 0
    else:
        i = 0
        if funct(a) * pohidna(a) < 0:
            x = a
        else:
            x = b
        if x == a:
            fix = b
        else:
            fix == a
        prev_x = fix
        while abs(prev_x - x) > eps:
            prev_x = x
            x = x - (funct(x) * (fix - x))/(funct(fix) - funct(x))
            i += 1
            print("i=%2i"%(i-1))
        return x
def newton(a, b, eps):
    if funct(a) * funct(b) > 0:
        return 0, 0
    else:
        i = 0
        if funct(a) * pohidna(a) < 0:
            x = a
        else:
            x = b
        if x == a:
            fix = b
        else:
            fix = a
        prev_x = fix
        while abs(prev_x - x) > eps:
            prev_x = x
            x = prev_x - funct(x)/pohidna(x)
            i += 1
            print("i=%2i"%(i-1))
        return x


def combined(a, b, eps):
    if funct(a) * funct(b) > 0:
        return 0, 0
    else:
        i = 0
        if funct(a) * pohidna(a) > 0:
            dumb = a
            a = b
            b = dumb
        while abs(b - a) > 2 * eps:
            b = b - (funct(b) * (b - a))/(funct(b) - funct(a))
            a = a - funct(a)/pohidna(a)
            i += 1
            print("i=%2i"%(i-1))
        return (a + b)/2

a = float(input('a: '))
b = float(input('b: '))
eps = float(input('eps: '))
result = chord(a, b, eps)
print("chord: %.5f"%(result))
result = newton(a, b, eps)
print("newton: %.5f"%(result))
result = combined(a, b, eps)
print("combined: %.5f"%(result))
