f = open('D:\data\\1.29-阳光---1.txt','r')
x = 0
Q = []
W = []
E = []
for i in f:
    x += 1

    if x%3 == 1:
        Q.append(i)
    elif x%3 == 2:
        W.append(i)
    elif x%3 == 0:
        E.append(i)

G = open("D:\data\\1.29-阳光---1_fenkai.txt",'a')


G.seek(0)
G.truncate()   #清空文件

for c in range(0,5000):
    G.write(Q[c])
  #  G.write('\n')

for v in range(0,5000):
    G.write(W[v])

for b in range(0,4999):
    G.write(E[b])