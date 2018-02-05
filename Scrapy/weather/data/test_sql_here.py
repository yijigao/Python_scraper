import sqlite3
from pprint import pprint

con = sqlite3.connect("weather_cd.db")
cur = con.cursor()
cur.execute('select * from my_weather WHERE week=="星期四" AND weather=="晴"' )
pprint(cur.fetchall())