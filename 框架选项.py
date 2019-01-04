import tkinter
import translation




root = tkinter.Tk()

root.title('by = 谭 勇')
#root.geometry('300x300')


var = ['111','222','333','444']

Frame = tkinter.LabelFrame(root,text = '选择以下几个!')

Frame.pack(padx = 20,pady = 20)



for x in var:
    v = tkinter.IntVar()

    C = tkinter.Checkbutton(Frame,text =x,variable = v)

    C.pack(anchor = 'center')




x = tkinter.IntVar()

tkinter.Radiobutton(Frame,text = '哈哈!',variable = x,value = 1).pack(anchor = 'n')
tkinter.Radiobutton(Frame,text = '呵呵!',variable = x,value = 3).pack(anchor = 'n')
tkinter.Radiobutton(Frame,text = '哦哦!',variable = x,value = 4).pack(anchor = 'n')

root.mainloop()