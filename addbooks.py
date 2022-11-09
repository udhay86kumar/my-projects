from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox,ttk
import pymysql

def bookRegister():
    count_book=[]
    department=bookinfo5.get()
    bid = bookinfo1.get()
    title = bookinfo2.get()
    author = bookinfo3.get()
    edition = bookinfo4.get()
    insertBooks = "insert into " + booktable + " values('" + department + "','" + bid + "','" + title + "','" + author + "','" + edition + "')"
    values="INSERT INTO count_books(title,author,edition) select title,author,edition from "+booktable
    allbook=[]
    try:
        cur.execute(insertBooks)
        con.commit()


        messagebox.showinfo('Success', "Book added successfully")
    except:
        messagebox.showinfo("Error", "Can't add data into Database")
    """
    try:
        countlist = "select title,author,edition from " + count
        cur.execute(countlist)
        con.commit()
        for i in cur:
            allbook.append(i[0])

        if bid in allbook:
            checkAvail = "select title from " + count + " where title='" + title + "'"
            cur.execute(checkAvail)
            con.commit()
            print(allbook)
    except:
         messagebox.showinfo("Error ")
         print(count_book)

    print(department)
    print(bid)
    print(title)
    print(author)"""


    try:

        #cur.execute(valuss)
        cur.execute(values)
        con.commit()

        print("excute the values ")

    except:
        messagebox.showinfo("search Error ","the value error")

def addBooks():
    global bookinfo5,bookinfo1, bookinfo2, bookinfo3, bookinfo4,booktable, convas1, con, cur, books, gui,count
    con = pymysql.connect(host="localhost", user="root", password="udhaya", database="mydatabase")
    cur = con.cursor()
    booktable = "bookss"
    count="count_books"
    gui = Tk()
    gui.title("Library")
    h =700
    w = 700
    sw = gui.winfo_screenwidth()
    sh =gui.winfo_screenheight()
    x = (sw / 2) - (w / 2)
    y = (sh / 2) - (h / 2)
    gui.geometry("%dx%d+%d+%d" % (w, h, x, y))

    convas1 = Canvas(gui)
    convas1.config(bg="lightyellow")
    convas1.pack(expand=True, fil=BOTH)
    # head Frame
    head = Frame(gui, bg="pink",bd=5)
    head.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    # head lebel
    headlabel = Label(head, text="Addbooks", bg="black", fg="white", font=('courier'))
    headlabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelframe = Frame(gui, bg="pink")
    labelframe.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    deparment=["Computer Science","Mathametics","Commerse","Tamil","English"]
    l1=Label(labelframe ,text="Select Department :",bg="black",fg="white")
    l1.place(relx=0.01, rely=0.06, relheight=0.08)

    bookinfo5=ttk.Combobox(labelframe,value=deparment,width=4)

    bookinfo5.place(relx=0.3,rely=0.05 ,relwidth=0.62,relheight=0.08)
    
    lb1 = Label(labelframe, text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)
    bookinfo1 = Entry(labelframe)
    bookinfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    lb2 = Label(labelframe, text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)
    bookinfo2 = Entry(labelframe)
    bookinfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    lb3 = Label(labelframe, text="Author Name : ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)
    bookinfo3 = Entry(labelframe)
    bookinfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    lb4 = Label(labelframe, text="Edition : ", bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.65, relheight=0.08)
    bookinfo4 = Entry(labelframe)
    bookinfo4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

    submitbtn = Button(gui, text="Submit", bg='#d1ccc0', fg='black',command=bookRegister)
    submitbtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitbtn = Button(gui, text="Quit", bg='#d1ccc0', fg='black', command=gui.destroy)
    quitbtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
    gui.mainloop()
addBooks()