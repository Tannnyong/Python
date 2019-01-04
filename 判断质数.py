number = input('请输入一个数字：')

number = int(number)
half = number // 2

print(half)


for num in range(2,half + 1):
    print(num)
    if number % num == 0:

        print(number,'不是质数')
        break
else:
    print(number,'是质数')