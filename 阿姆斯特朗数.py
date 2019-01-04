for i in range(1,10):
#    print('i = ',i)
    for a in range(0,10):
#        print('a = ',a)
        for b in range(0,10):
#          print('b = ',b)
            x = i*100+a*10+b
            if x == i*i*i+a*a*a+b*b*b:
                print(i,a,b,'=',i,'^3+',a,'^3+',b,'^3')