# Find LCM Betwen Two Numbers
# Formula: : LCM(a, b) = a * b / GCD(a, b)


def gcd(a, b):
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return a + b

def lcm(a, b):
    return (a * b) // gcd(a, b)

print("LCM of 12 and 15 is:", lcm(12, 15))