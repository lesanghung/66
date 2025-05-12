from tkinter import *
from tkinter.ttk import *
main = Tk()
main.title("project nhóm 1")
main.geometry("400x400")
lbl= Label(main,text= "Data ", font= 'arial 15 bold' )

lbl.place(x=50,y=10)
lbl2= Label(main,text= "remove ", font= 'arial 15 bold' )
lbl2.place(x=150,y=10)
lbl3= Label(main,text= "filter", font= 'arial 15 bold' )
lbl3.place(x=240,y=10)
lbl4= Label(main,text= "undo", font= 'arial 15 bold' )
lbl4.place(x=300,y=10)
def click():
    lbl5=Label (main,text="section")
    lbl5.pack()
btn=Button(main, text =" Button ",command =click,compound= 'bottom')
btn.place(x=150, y=50)
def get():
    data=entry.get()
    lbl.config(text="type File"+data)
entry=Entry(main,font='arial 15 bold',width=10)


entry.place(x=100, y=100)


lbl=Label(main,text=" ")
lbl.place(x=100,y=200)
btn1=Button(main,text="Đăng nhập",command=get)
btn1.place(x=90,y=120)



main.mainloop()

