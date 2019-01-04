
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


#输入数据
X = np.array([[1,2,3],
              [1,6,3],
              [1,1,1],
              [1,4,9],
              [1,4,3],
              [1,1,2]])
#标签
Y = np.array([1,1,-1,1,-1,-1])
#权值初始化 一行三列 取值范围 -1 1
W = (np.random.random(3)-0.5)*2
print(W)


# In[3]:


#学习效率设置
LR = 0.11

#记录迭代次数
n = 0

#神经网络的输出
o = 0

def updata():
    global X,Y,W,LR,n
    n += 1
  #  o = np.sign(np.dot(X,W.T))
    o =np.dot(X,W.T)
    WC = LR * ((Y - o.T).dot(X))/ int(X.shape[0])
    W = W + WC


# In[4]:


for _ in range(1000):
    updata()  #更新权值
    print(W)  #打印当前权值
    print(n)   #打印迭代次数
    o = np.sign(np.dot(X,W.T)) #计算当前输出
    if (o == Y.T).all():  #如果实际输出等于期望输出
        print('Finished')
        print('epoch',n)
        break


# In[5]:


#正样本
x1 = [2,6,4]
y1 = [3,3,9]
#负样本
x2 = [1,2,4]
y2 = [1,1,3]


k = -W[1]/W[2]
d = -W[0]/W[2]

print('k = ',k)
print('d = ',d)

xdata = np.linspace(0,5)

plt.figure()
plt.plot(xdata,xdata*k+d,'r')
plt.plot(x1,y1,'bo')
plt.plot(x2,y2,'yo')
plt.show()

