import mysql.connector
mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password ="udhaya",
      database="mydatabase"
)
mycurser = mydb.cursor()
#sql="INSERT INTO borrow_books( BookUser,UserId,UserName,BookName,AuthorName,Edition) values('student','12','udhaya','java1','python','2')"
#val=("java1","udhaykumar","3")
#mycurser.execute("CREATE TABLE borrow_books(bid INT AUTO_INCREMENT PRIMARY KEY,booksuser Varchar(50),username varchar(50), varchar(20))")
#mycurser.execute("ALTER TABLE count_books UPDATE COLUMN edition INT")
#mycurser.execute("SELECT *,COUNT(*) \ From count_books \GROUP BY title,author,edition \HAVING COUNT(*) > 1;")
#sql="select status from coun_books where title='python',author='guido',edition='2'"
mycurser.execute("select * from borrow_books")
myresult = mycurser.fetchall()

for x in myresult:
   print(x)
