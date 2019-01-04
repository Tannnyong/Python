import tkinter
import webbrowser

root = tkinter.Tk()
root.title("by : 谭勇")


x = tkinter.Text(root,width = 40 ,height = 5)
x.pack()


x.insert('insert',"查询请点击： www.baidu.com")
x.pack(anchor = 'center' , padx = '5' , pady = '5')

x.tag_add("link","1.7","1.20")
x.tag_config("link",foreground = "blue" , underline = "t")

def aa():
    x.config(cursor = 'arrow')
def bb():
    x.config(curior = 'xterm')
def cc():
    webbrowser.open("http://www.baidu.com")



x.tag_bind("link",'Enter',aa)
x.tag_bind("link","leave",bb)
x.tag_bind("link","Button-1",cc)

root.mainloop()