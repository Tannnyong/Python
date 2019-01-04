import random
number = 0
i = 0
while  number!=5:
    number = int(random.uniform(0,9))
    print(number)
    i += 1
else:
    print('失败了，坚持了',i,'次')
