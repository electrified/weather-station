import sqlite3
from sqlite3 import Error
import datetime
import temp
import time

def sql_connection():
    try:
        con = sqlite3.connect('weather.db')
        return con
    except Error:
        print(Error)
 
def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("create table if not exists reading(id integer PRIMARY KEY AUTOINCREMENT, sensor text, raw_value real, created_at datetime)")
    con.commit()

def drop_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("drop table if exists reading")
    con.commit()

def insert_record(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO reading(sensor, raw_value, created_at) VALUES(?, ?, ?)', entities)
    con.commit()

con = sql_connection()
# drop_table(con)
sql_table(con)


while True:
    #print(read_temp())  
    entities = ('INSIDE_TEMP', temp.read_temp()[0], datetime.datetime.now())
    insert_record(con,entities)
    time.sleep(30)

