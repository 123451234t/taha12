import sqlite3
class student:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS student(id integer praimary key , name text,lname text,password text , dore text)")        
        self.con.commit()

    def insert(self,name,lname,password,dore):
        self.cur.execute("INSERT INTO student VALUES(NULL,?,?,?,?)",(name,lname,password,dore))
        self.con.commit()

    def select(self):
        self.cur.execute("select * from student")
        return self.cur.fetchall()

    def delet(self,id):
        self.cur.execute("DELET * FROM student where id = ?",(id,))
        self.con.commit()

    





