import tkinter
import translation



root = tkinter.Tk()

root.title('by = 谭 勇 ， 功能 = 翻译')
#root.geometry('400x200')

a = tkinter.Label(root,text = '原 文:')
a.grid(row = 0 , column = 0)
b = tkinter.Label(root,text = '翻 译:')
b.grid(row = 1,column = 0)


x = tkinter.Entry(root)
x.grid(row = 0,column = 1,padx = 10,pady = 10,ipadx = 100)
y = tkinter.Entry(root)
y.grid(row = 1,column = 1,padx = 10,pady = 10,ipadx = 100)

def Fanyi():
    Str = x.get()
    JG = translation.Tran(Str)
    y.delete(0,10000)
    y.insert(0,JG)

c = tkinter.Button(root,text = '点击翻译' ,width=15, height=2,command = Fanyi)
c.grid(row = 2,column = 0,padx = 10,pady = 10,stick = 'w')
d = tkinter.Button(root,text = '退出软件' ,width=15, height=2,command =root.quit())
d.grid(row = 2,column = 1,padx = 10,pady = 10,stick = 'e')
#Get = Tran()


#x.inset(0, get)


root.mainloop()