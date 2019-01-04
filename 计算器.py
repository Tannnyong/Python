import tkinter

root = tkinter.Tk()
root.title('by = 谭勇 功能 = 计算器')
v1 = tkinter.StringVar()
v2 = tkinter.StringVar()
v3 = tkinter.StringVar()

Fram = tkinter.Frame(root)
Fram.pack(padx = 10,pady = 10)


def test(content):
    return content.isdigit()


testCMD = root.register(test)

x1 = tkinter.Entry(Fram,
                   textvariable = v1,                  #文本框的值，是一个StringVar()对象
            #      bg = 'red',                         #背景颜色 background(bg)
            #      bd =  10  ,                         #宽度  borderwidth(bd)
            #      font = ('黑体','10','bold'),        #文字字体。值是一个元祖，font = ('字体'，'字号'，'粗细')
            #      foreground = 'yellow',              #文字颜色。值为颜色或为颜色代码，如：'red','#ff0000'
            #      highlightcolor = 'red',             #文本框高亮边框颜色，当文本框获取焦点时显示
            #      show = '@',                         #隐藏信息显示
            #      state = 'disabled',                 #文框状态，分为只读和可写，值为：normal/disabled/readonly

                   validate = "key",                   #focus：当entry组件获得或者失去焦点的时候验证
                                                       # focusin：当entry组件获得焦点的时候验证
                                                       # focusout:当entry组件失去焦点的时候验证
                                                       # key:当输入框被编辑的时候验证
                                                       # all:当出现上面任何一种情况时候验证
                                                       # none:关闭验证功能。默认设置为该选项
                   validatecommand=(testCMD,'%P')
                                                       #  validatecommand选项指定一个验证函数，该函数只能返回True或者False表示验证结果，
                                                       # 一般情况下验证函数只需要知道输入框中的内容即可，可以通过Entry组件的get()方法来获得该字符串。
                                                       # 最后invalidcommand选项指定的函数只有在validatecommand的返回值为False的时候才被调用。
                                                       # %P表示 当输入框的值允许改变，该值有效。该值为当前文本框内容
                                                       # %v(小写大写不一样的)，当前validate的值
                                                       # %W表示该组件的名字



                   )
x1.grid(row = 0,column = 0,padx = 10,pady = 10)
x2 = tkinter.Label(Fram,text = ' + ')
x2.grid(row = 0,column = 1,padx = 10,pady = 10)
x3 = tkinter.Entry(Fram,
                   textvariable = v2,
                   validate = "key",
                  validatecommand = (testCMD, '%P')


                   )
x3.grid(row = 0,column = 2,padx = 10,pady = 10)
x2 = tkinter.Label(Fram,text = ' = ')
x2.grid(row = 0,column = 3,padx = 10,pady = 10)
x4 = tkinter.Entry(Fram,textvariable = v3,state = 'readonly')
x4.grid(row = 0,column = 4,padx = 10,pady = 10)

def aaa():
    bbb = int(v1.get())+int(v2.get())
    v3.set(bbb)

x5 = tkinter.Button(Fram,text = '开始计算',command = aaa)
x5.grid(row = 1,column = 2,padx = 10,pady = 10)
root.mainloop()