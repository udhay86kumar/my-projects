from tkinter import *
from PIL import ImageTk ,Image
from pymysql import *
from addbooks import *
from Borrow_Book import *
from Return_Book import *
from count_books import *


gui=Tk()
gui.title("Library Menagement system")
background_image = Image.open("lib.jpg")

h=700
w=700
sw = gui.winfo_screenwidth()
sh=gui.winfo_screenheight()
x = (sw/2)-(w/2) 
y=(sh/2)-(h/2)
gui.geometry("%dx%d+%d+%d"%(w,h,x,y))
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(gui)
#Canvas1.create_image(300, 340, image=img)
Canvas1.config(bg="white", width=sw, height=sh)
Canvas1.pack(expand=True, fill=BOTH)

headingFrame1 = Frame(gui, bg="#FFBB00", bd=5)
headingLabel = Label(headingFrame1, text="Welcome to Library", bg='yellow', fg='Blue', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
btn1 = Button(gui,text="Add Book Details",bg="pink",fg="white",command=addBooks)
btn1.place(relx=0.28,rely=0.3,relwidth=0.45,relheight=0.1)
btn2 = Button(gui,text="Borrow Book",bg="pink",fg="white",command=B_book)
btn2.place(relx=0.28,rely=0.4,relwidth=0.45,relheight=0.1)
btn3 = Button(gui,text="View Booklist",bg="pink",fg="white")
btn3.place(relx=0.28,rely=0.5,relwidth=0.45,relheight=0.1)
btn4 = Button(gui,text="Retrun Book",bg="pink",fg="white",command=return_book)
btn4.place(relx=0.28,rely=0.6,relwidth=0.45,relheight=0.1)

btn5 = Button(gui,text="Count Book",bg="pink",fg="white",command=C_books)
btn5.place(relx=0.28,rely=0.7,relwidth=0.45,relheight=0.1)

gui.mainloop()


