a = input('请输入字符串：')

a = str(a)

print('a = ',a)

c=[]

c=a.split(' ')

print('c = ',c)

b = set(c)


print('b = ',b)

print('输入的字符串不重复的有：',b)

#用count（）的方法
a = input('请输入字符串：')
c = input('请输入需要查询次数的字符串：')

b = []
print('b = ',b)

b = a.split(' ')
print('b = ',b)


d=b.count(c)    # str.count(sub, start= 0,end=len(string))
                # Python count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。

print(d)



