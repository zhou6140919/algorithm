num1 = 3141592653589793238462643383279502884197169399375105820974944592
num2 = 2718281828459045235360287471352662497757247093699959574966967627

# num1 = 1234
# num2 = 5678

m = len(str(num1))

assert m % 2 == 0
assert m == len(str(num2))


def mult(num1, num2):
    n = max(len(str(num1)), len(str(num2)))
    nl = min(len(str(num1)), len(str(num2)))

    if nl == 1:
        return num1*num2
    a = num1 // pow(10, n//2)
    b = num1 % pow(10, n//2)
    # print('a, b:', a, b)
    c = num2 // pow(10, n//2)
    d = num2 % pow(10, n//2)
    # print('c, d:', c, d)

    ac = mult(a, c)
    bd = mult(b, d)
    ad = mult(a, d)
    bc = mult(b, c)

    ans = pow(10, n)*ac+pow(10, n//2)*(ad+bc)+bd

    return ans


a = mult(num1, num2)
# a = num1*num2
print('right answer', num1*num2)
print('my answer', a)
