import tkinter

root = tkinter.Tk()

x =tkinter.Scrollbar(root)
x.pack(side ='right',fill = 'y')

y = tkinter.Listbox(root,yscrollcommand = x.set)

for i in range(1000):
    y.insert('end',i)

y.pack()

x.config(command = y.yview)

def aaa():
    y.delete("active")

z = tkinter.Button(root,text = '点击删除',command  = aaa)
z.pack()
root.mainloop()