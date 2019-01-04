a = input('请输入字符串：')
c = input('请输入需要查询次数的字符串：')
x = c
print('x = ',x)

i = 0
b = []
print('b = ',b)

b = a.split(' ')
print('b = ',b)

for g in b:
    if x==g:
        i += 1

print(x, '所出现的次数为', i)

