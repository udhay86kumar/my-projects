import tkinter
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql
gui = Tk()

def borrow_book():
    global Result,cur

    Department=bookinfo.get()
    BookUser =bookinfo1.get()
    UserId = bookinfo2.get()
    user_name= bookinfo3.get()
    book_name = bookinfo4.get()
    Author_name=bookinfo5.get()
    edition= bookinfo6.get()

    con = pymysql.connect(host="localhost", user="root", password="udhaya", database="mydatabase")
    cur = con.cursor()
    Borrow_book="borrow_books"
    #try:
    count="insert into " + Borrow_book + " values('" + Department + "','" + BookUser + "','" + UserId + "','" + user_name + "','" + book_name + "','" +  Author_name + "','" + edition + "')"
    try:
        cur.execute(count)
        con.commit()
        messagebox.showinfo('Success', "Book added successfully")

    except:
        messagebox.showinfo("Error", "Can't add data into Database")


    delete_book = "delete from count_books where title='" + book_name + "', author= '" + Author_name + "', edition= '" + edition + "'"
    try:
        cur.execute(delete_book)
        con.commit()
        messagebox.showinfo("deleted count books table")
    except:

        print("Not delected ")

def B_book():
    global bookinfo,bookinfo1,bookinfo2,bookinfo3,bookinfo4,bookinfo5,bookinfo6,con,gui,Result,student_table,cur

    gui.title("Library")
    gui.geometry("1350x700+0+0")
    """      
    h = 900
    w = 900
    sw = gui.winfo_screenwidth()
    sh = gui.winfo_screenheight()
    x = (sw / 2) - (w / 2)
    y = (sh / 2) - (h / 2)
    gui.geometry("%dx%d+%d+%d" % (w, h, x, y))
    """
    gui.config(bg="lightgreen")
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", bg="lightred", fg="black", rowheight=25, fieldbackground="white")

    style.map(gui, "Treeview", background=["selected", "darkred"])
    title = Label(gui, text="Borrow Book", font=("Arial", 20, "bold"), padx=15, pady=15, border=0,relief=tkinter.GROOVE, bg="teal", fg="white")
    title.pack(side=tkinter.TOP, fill=tkinter.X)
    # title_label = Label(gui,text="Staff",font=("Arial", 20, "bold"),padx=15,pady=15,   border=0, relief=tkinter.GROOVE, bg="teal",  foreground="white")
    # title_label.pack(side=tkinter.TOP, fill=tkinter.X)
    # global Detail,gui,btn1
    Detail = LabelFrame(gui, text="Book Records", font=("Arial", 14), bg="lightpink", fg="black", relief=tkinter.GROOVE)
    Detail.place(x=5, y=80, width=450, height=600)
    # Borrow book detailsuser
    id_lab1 = Label(Detail, text=" Department :", font=("Arial", 16), bg="lightpink", fg="black")
    id_lab1.place(x=30, y=15)
    tree_ent = ["Computer Science","Maths","Tamil","English","Commerce"]
    bookinfo = ttk.Combobox(Detail, font=("arial", 12), values=tree_ent)
    bookinfo.place(x=200, y=20, width=200, height=25)

    id_lab1 = Label(Detail, text="Book User :", font=("Arial", 16), bg="lightpink", fg="black")
    id_lab1.place(x=30, y=60)
    tree_ent = ["Staff", "Student"]
    bookinfo1 = ttk.Combobox(Detail,font=("arial", 12),values=tree_ent)
    bookinfo1.place(x=200, y=60, width=200, height=25)

    stname = Label(Detail, text="User Id :", font=("Arial", 16), bg="lightpink", fg="black")
    stname.place(x=30, y=100)
    bookinfo2 = Entry(Detail, bd=1, font=("arial", 12), bg="white", fg="black")
    bookinfo2.place(x=200, y=102,width=200, height=25)

    id_book = Label(Detail, text="User Name :", font=("Arial", 16), bg="lightpink", fg="black")
    id_book.place(x=30, y=143)
    bookinfo3 = Entry(Detail, bd=1, font=("arial", 12), bg="white", fg="black")
    bookinfo3.place(x=200, y=145, width=200, height=25)

    Bname = Label(Detail, text="Book Name :", font=("Arial", 16), bg="lightpink", fg="black")
    Bname.place(x=30, y=187)
    bookinfo4 = Entry(Detail, bd=1, font=("arial", 12), bg="white", fg="black")
    bookinfo4.place(x=200, y=190, width=200, height=25)

    Aname = Label(Detail, text="Author Name :", font=("Arial", 16), bg="lightpink", fg="black")
    Aname.place(x=30, y=227)
    bookinfo5 = Entry(Detail, bd=1, font=("arial", 12), bg="white", fg="black")
    bookinfo5.place(x=200, y=233, width=200, height=25)

    edition = Label(Detail, text="Edition No :", font=("Arial", 16), bg="lightpink", fg="black")
    edition.place(x=30, y=273)
    bookinfo6= Entry(Detail, bd=1, font=("arial", 12), bg="white", fg="black")
    bookinfo6.place(x=200, y=275, width=200, height=25)

    sbtn1 = Button(Detail, text="Submit", bg="lightgreen", fg="black", padx=10, pady=10, bd=1, command=borrow_book)
    sbtn1.place(x=100, y=350, width=100, height=60)
    q_btn2 = Button(Detail, text="Quit", bg="lightgreen", fg="black", padx=10, pady=10, bd=1, command=gui.destroy)
    q_btn2.place(x=250, y=350, width=100, height=60)
    main_frame = LabelFrame(gui,bg="lightpink",bd=2,relief=tkinter.GROOVE)
    main_frame.place(x=460, y=80, width=880, height=600)

    y_scroll = tkinter.Scrollbar(main_frame, orient=tkinter.VERTICAL)
    x_scroll = tkinter.Scrollbar(main_frame, orient=tkinter.HORIZONTAL)

    # Treeview database

    student_table = ttk.Treeview(main_frame, columns=(
       "Department","Book User", "User Id","User name","Book Name","Author Name", "Edition No"
    ), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

    y_scroll.config(command=student_table.yview)
    x_scroll.config(command=student_table.xview)

    y_scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    x_scroll.pack(side=tkinter.BOTTOM, fill=tkinter.X)

    student_table.heading("Department", text="Department")
    student_table.heading("Book User", text="Book User")
    student_table.heading("User Id", text="User Id")
    student_table.heading("User name", text="User name")
    student_table.heading("Book Name", text="Book Name")
    student_table.heading("Author Name", text="Author Name")
    student_table.heading("Edition No", text="Edition No")

    student_table["show"] = "headings"

    student_table.column("Department", width=100)
    student_table.column("Book User", width=100)
    student_table.column("User Id", width=100)
    student_table.column("User name", width=100)
    student_table.column("Book Name", width=100)
    student_table.column("Author Name", width=100)
    student_table.column("Edition No", width=100)
    student_table.pack(fill=tkinter.BOTH, expand=True)
    student_table.tag_configure("oddrow", background="yellow")
    student_table.tag_configure("evenrow", background="green")
    con = pymysql.connect(host="localhost", user="root", password="udhaya", database="mydatabase")
    cur = con.cursor()
    allbook = "select * from borrow_books"
    cur.execute(allbook)
    con.commit()
    Result=cur.fetchall()
    count = 0
    for record in Result:
        if count % 2 == 0:
            student_table.insert(parent="", index="end", iid=count, text="", values=(
                record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=("evenrow"))
        else:
            student_table.insert(parent="", index="end", iid=count, text="", values=(
                record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=("oddrow"))

        count += 1
    student_table.tag_configure("evenrow", background="yellow")
    student_table.tag_configure("oddrow", background="green")

    """def Staff_Book():
        global Detail,gui,btn1
        Detail=LabelFrame(gui,text="Book Records",font=("Arial",14),bg="lightpink",fg="black",relief=tkinter.GROOVE)
        Detail.place(x=2,y=120,width=450,height=550)
        id_lab1=Label(Detail,text="Staff Id :",font=("Arial",16),bg="lightpink",fg="black")
        id_lab1.place(x=30,y=5)
        stid=Entry(Detail,bd=1,font=("arial",16),bg="white",fg="black")
        stid.place(x=200,y=8,width=200,height=20)
        stname=Label(Detail,text="Staff Name :",font=("Arial",16),bg="lightpink",fg="black")
        stname.place(x=30,y=40)
        st_name=Entry(Detail,bd=1,font=("arial",16),bg="white",fg="black")
        st_name.place(x=200,y=45,width=180,height=20)
    #Borrow book details
        id_book1=Label(Detail,text="Book Id :",font=("Arial",16),bg="lightpink",fg="black")
        id_book1.place(x=30,y=76)
        Bid1=Entry(Detail,bd=1,font=("arial",16),bg="white",fg="black")
        Bid1.place(x=200,y=80,width=180,height=20)
        Bname1=Label(Detail,text="Book Name :",font=("Arial",16),bg="lightpink",fg="black")
        Bname1.place(x=30,y=110)
        s_name1=Entry(Detail,bd=1,font=("arial",16),bg="white",fg="black")
        s_name1.place(x=200,y=117,width=180,height=20)
        edition = Label(Detail, text="Edition No :", font=("Arial", 16), bg="lightpink", fg="black")
        edition.place(x=30, y=150)
        e_name = Entry(Detail, bd=1, font=("arial", 16), bg="white", fg="black")
        e_name.place(x=200, y=150, width=180, height=20)

        sbtn = Button(Detail, text="Submit", bg="lightgreen", fg="black", padx=10, pady=10, bd=1)
        sbtn.place(x=100, y=250, width=100, height=60)
        q_btn1 = Button(Detail, text="Quit", bg="lightgreen", fg="black", padx=10, pady=10, bd=1,command=gui.destroy)
        q_btn1.place(x=250, y=250, width=100, height=60)


    btn1=Button(gui,text="STAFF",bg="blue",fg="black",padx=10,pady=10,bd=2,relief=tkinter.GROOVE,command=Staff_Book)
    btn1.place(x=0,y=60,width=500,height=50)
    btn2=Button(gui,text="STUDENT",bg="blue",fg="black",padx=10,pady=10,bd=2,relief=tkinter.GROOVE,command=Student_book)
    btn2.place(x=501,y=60,width=500,height=50)
    """

    gui.mainloop()
B_book()