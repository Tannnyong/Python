

def Fibonacci (n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        number = Fibonacci(n - 1)+ Fibonacci(n - 2)
        return number

n = input('请输入所求兔子数的月数N：')

n = int(n) + 1
number = int(Fibonacci(n))

print(number)


'''
m = input('输入所求斐波拉契数列个数M：')

m = int(m) - 1
v = 0
if m == 0:
    print('1')
elif m == 1:
    print('1')
else:
    for c in range(0,m+1):
        if c == 0:
            d = 1
            print(d)
        elif c ==1:
            f = 1
            print(f)
        else:
            v = f + d
            k = f
            f = v
            d = k


            print(v)
'''