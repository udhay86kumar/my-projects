import tkinter
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql

def C_books():
    global count, result

    con = pymysql.connect(host="localhost", user="root", password="udhaya", database="mydatabase")
    cur = con.cursor()
    try:
        count_bookss = "SELECT *,COUNT(*) \
                 From count_books \
                 GROUP BY title,author,edition \
                 HAVING COUNT(*) > 1;;"
        # cur.execute(valuss)
        cur.execute(count_bookss)
        con.commit()
        result = cur.fetchall()


    except:
        messagebox.showinfo("search Error ", "the value error")

    gui = Tk()
    gui.title("Library")
    gui.geometry("1350x700+0+0")
    gui.config(bg="lightpink")
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", bg="lightblues", fg="black", rowheight=25, fieldbackground="white")

    style.map(gui, "Treeview", background=["selected", "darkred"])
    title = Label(gui, text="Count Book", font=("Arial", 20, "bold"), padx=15, pady=15, border=0, relief=tkinter.GROOVE,
                  bg="teal", fg="white")
    title.pack(side=tkinter.TOP, fill=tkinter.X)
    main_frame = LabelFrame(gui,bg="lightpink",bd=2, relief=tkinter.GROOVE)
    main_frame.place(x=70, y=80, width=1200, height=600)

    y_scroll = tkinter.Scrollbar(main_frame, orient=tkinter.VERTICAL)
    x_scroll = tkinter.Scrollbar(main_frame, orient=tkinter.HORIZONTAL)
    BOOK_table = ttk.Treeview(main_frame, columns=(  "Book Name", "Author Name", "Edition", "Book Counts" ), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

    y_scroll.config(command=BOOK_table.yview)
    x_scroll.config(command=BOOK_table.xview)

    y_scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    x_scroll.pack(side=tkinter.BOTTOM, fill=tkinter.X)


    BOOK_table.heading("Book Name", text="Book Name")
    BOOK_table.heading("Author Name", text="Author Name")
    BOOK_table.heading("Edition", text="Edition")
    BOOK_table.heading("Book Counts", text="Book Counts")
    BOOK_table["show"] = "headings"
    BOOK_table.column("Book Name", width=50)
    BOOK_table.column("Author Name", width=50)
    BOOK_table.column("Edition", width=50)
    BOOK_table.column("Book Counts", width=50)

    BOOK_table.pack(fill=tkinter.BOTH, expand=True)

    BOOK_table.tag_configure("oddrow", background="yellow")
    BOOK_table.tag_configure("evenrow", background="green")
    count = 0
    for record in result:
        if count % 2 == 0:
            BOOK_table.insert(parent="", index="end", iid=count, text="", values=(
             record[1], record[2], record[3],record[4]), tags=("evenrow"))
        else:
            BOOK_table.insert(parent="", index="end", iid=count, text="", values=(
            record[1], record[2], record[3],record[4]), tags=("oddrow"))

        count += 1
    BOOK_table.tag_configure("evenrow", background="yellow")
    BOOK_table.tag_configure("oddrow", background="green")

    q_btn1 = Button(gui, text="Quit", bg="lightgreen", fg="black", padx=10, pady=10, bd=1, command=gui.destroy)
    q_btn1.place(x=550, y=600, width=100, height=60)

    gui.mainloop()
C_books()