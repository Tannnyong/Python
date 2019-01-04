import tkinter
from PIL import Image, ImageTk
root = tkinter.Tk()

root.title('by: 谭 勇 ')

root.geometry("600x600")



def Accc():
    Format = tkinter.Label(root,

                           #                   fg = 'red',
                           #                   bg = 'blue',
                           #                  text = 'Hello I am Tkinter',
                           #                  width = 102,
                           #                   height = 3,
                           #                   compound = 'left',

                           text='想要人生过得去，生活必须带点绿',
                           bg='green',
                           width=40,
                           height=3,
                           wraplength=80,

                           )
    load = Image.open('C:\\Users\\tanyong\\Desktop\\1.jpg')  # 我图片放桌面上
    render = ImageTk.PhotoImage(load)

    img = tkinter.Label(root, image=render)
    img.image = render
    img.place(x=0, y=0)
    img.pack()

    Format.pack()
    root.mainloop()


on_hit = False  # 默认初始状态为 False
def hit_me():
    global on_hit
    if on_hit == False:     # 从 False 状态变成 True 状态
        on_hit = True
        Accc() # 设置标签的文字为 'you hit me'
    else:       # 从 True 状态变成 False 状态
        on_hit = False
        # 设置 文字为空


AAA = tkinter.Button(root,
                     text='点击我，送你个惊喜',  # 显示在按钮上的文字
                     width=15, height=2,
                     command=hit_me  # 点击按钮式执行的命令





)




AAA.pack()
root.mainloop()






