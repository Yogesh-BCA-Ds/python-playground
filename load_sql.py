import sqlite3
import pandas as pd
conn = sqlite3.connect("OnePiece.db") # creates the data base if not exits
                                      # or use if its exists
cursor = conn.cursor() # to write sql commands
'''
cursor needed for create table 
insert
update
'''

cursor.execute("""
create table if not exists student(
id INTEGER,
name TEXT,
marks INTEGER)
""")

cursor.execute("insert into student values (?,?,?)",(1,'luffy',100))
cursor.executemany("insert into student values (?,?,?)",
[
(2,'zoro',100),
(3,'sanji',100),
(4,'usoop',100)
])
conn.commit()

df = pd.read_sql("select * from student",conn)
print(df)
conn.close()
