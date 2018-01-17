import sqlite3


con = sqlite3.connect("yijigao.db")
cur = con.cursor()
cur.execute("create table people (name_last, age)")

who = "Yi Jigao"
age = 26

cur.execute("insert into people values (?, ?)",(who, age))

cur.execute("select * from people WHERE name_last=:who and age=:age", {"who": who, "age":age})

print(cur.fetchone())