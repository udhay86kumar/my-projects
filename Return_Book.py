import tkinter
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql
alluserid=[]
def return_book1():
  global bookinfo, bookinfo1, bookinfo2, bookinfo3, bookinfo4, bookinfo5, bookinfo6, con, gui, Result, student_table, cur,count_books,check,status
  Borrow_table='borrow_books'
  count_books="count_books"

  bid = bookinfo2.get()

  extractBid = "select UserId from " + Borrow_table
  try:
    cur.execute(extractBid)
    con.commit()
    for i in cur:
      alluserid.append(i[0])

    if bid in alluserid:
      checkAvail = "select status from " + Borrow_table + " where UserId = '" + bid + "'"
      cur.execute(checkAvail)
      con.commit()
      for i in cur:
        check = i[0]

      if check == 'avail':
        status = True
      else:
        status = False

    else:
      messagebox.showinfo("Error", "Book ID not present")
  except:
    messagebox.showinfo("Error", "Can't fetch Book IDs")

  issueSql = "delete from " +Borrow_table + " where bid = '" + bid + "'"

  print(bid in alluserid)

  updateStatus = "update " + count_books + " set status = 'avail' where UserId = '" + bid + "'"
  try:
    if bid in alluserid and status == True:
      cur.execute(issueSql)
      con.commit()
      cur.execute(updateStatus)
      con.commit()
      messagebox.showinfo('Success', "Book Returned Successfully")
    else:
      alluserid.clear()
      messagebox.showinfo('Message', "Please check the book ID")
      gui.destroy()
      return
  except:
    messagebox.showinfo("Search Error", "The value entered is wrong, Try again")

  alluserid.clear()
  gui.destroy()



def return_book():
  global bookinfo, bookinfo1, bookinfo2, bookinfo3, bookinfo4, bookinfo5, bookinfo6, con, gui, Result, student_table, cur, count_books
  gui = Tk()

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

  gui.config(bg="lightpink")
  style = ttk.Style()
  style.theme_use("default")
  style.configure("Treeview", bg="lightblues", fg="black", rowheight=25, fieldbackground="white")

  style.map(gui, "Treeview", background=["selected", "darkred"])
  title = Label(gui, text="Return Book", font=("Arial", 20, "bold"), padx=15, pady=15, border=0, relief=tkinter.GROOVE,
                bg="teal", fg="white")
  title.pack(side=tkinter.TOP, fill=tkinter.X)
  # title_label = Label(gui,text="Staff",font=("Arial", 20, "bold"),padx=15,pady=15,   border=0, relief=tkinter.GROOVE, bg="teal",  foreground="white")
  # title_label.pack(side=tkinter.TOP, fill=tkinter.X)
  # global Detail,gui,btn1
  Detail = LabelFrame(gui, text="Return Book Records", font=("Arial", 14), bg="lightblue", fg="black", relief=tkinter.GROOVE)
  Detail.place(x=5, y=80, width=450, height=600)
  # Borrow book detailsuser
  id_lab1 = Label(Detail, text=" Department :", font=("Arial", 16), bg="lightblue", fg="black")
  id_lab1.place(x=30, y=15)
  tree_ent = ["Computer Science", "Maths", "Tamil", "English", "Commerce"]
  bookinfo = ttk.Combobox(Detail, font=("arial", 12), values=tree_ent)
  bookinfo.place(x=200, y=20, width=200, height=25)

  id_lab1 = Label(Detail, text="Book User :", font=("Arial", 16), bg="lightblue", fg="black")
  id_lab1.place(x=30, y=60)
  tree_ent = ["Staff", "Student"]
  bookinfo1 = ttk.Combobox(Detail, font=("arial", 12), values=tree_ent)
  bookinfo1.place(x=200, y=60, width=200, height=25)

  stname = Label(Detail, text="User Id :", font=("Arial", 16), bg="lightblue", fg="black")
  stname.place(x=30, y=100)
  bookinfo2 = Entry(Detail, bd=1, font=("arial", 12), bg="white", fg="black")
  bookinfo2.place(x=200, y=102, width=200, height=25)

  id_book = Label(Detail, text="User Name :", font=("Arial", 16), bg="lightblue", fg="black")
  id_book.place(x=30, y=143)
  bookinfo3 = Entry(Detail, bd=1, font=("arial", 12), bg="white", fg="black")
  bookinfo3.place(x=200, y=145, width=200, height=25)

  Bname = Label(Detail, text="Book Name :", font=("Arial", 16), bg="lightblue", fg="black")
  Bname.place(x=30, y=187)
  bookinfo4 = Entry(Detail, bd=1, font=("arial", 12), bg="white", fg="black")
  bookinfo4.place(x=200, y=190, width=200, height=25)

  Aname = Label(Detail, text="Author Name :", font=("Arial", 16), bg="lightblue", fg="black")
  Aname.place(x=30, y=227)
  bookinfo5 = Entry(Detail, bd=1, font=("arial", 12), bg="white", fg="black")
  bookinfo5.place(x=200, y=233, width=200, height=25)

  edition = Label(Detail, text="Edition No :", font=("Arial", 16), bg="lightblue", fg="black")
  edition.place(x=30, y=273)
  bookinfo6 = Entry(Detail, bd=1, font=("arial", 12), bg="white", fg="black")
  bookinfo6.place(x=200, y=275, width=200, height=25)

  sbtn1 = Button(Detail, text="Submit", bg="lightgreen", fg="black", padx=10, pady=10, bd=1)
  sbtn1.place(x=100, y=350, width=100, height=60)
  q_btn2 = Button(Detail, text="Quit", bg="lightgreen", fg="black", padx=10, pady=10, bd=1, command=gui.destroy)
  q_btn2.place(x=250, y=350, width=100, height=60)
  main_frame = LabelFrame(gui, bg="lightpink", bd=2, relief=tkinter.GROOVE)
  main_frame.place(x=460, y=80, width=880, height=600)

  y_scroll = tkinter.Scrollbar(main_frame, orient=tkinter.VERTICAL)
  x_scroll = tkinter.Scrollbar(main_frame, orient=tkinter.HORIZONTAL)

  # Treeview database

  student_table = ttk.Treeview(main_frame, columns=(
    "Department", "Book User", "User Id", "User name", "Book Name", "Author Name", "Edition No"
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
  Result=[]
  count = 0
  for record in Result:
    if count % 2 == 0:
      student_table.insert(parent="", index="end", iid=count, text="", values=(
        record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=("evenrow"))
    else:
      student_table.insert(parent="", index="end", iid=count, text="", values=(
        record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=("oddrow"))

    count += 1
  gui.mainloop()
return_book()

