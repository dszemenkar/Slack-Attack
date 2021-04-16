import sqlite3
from datetime import datetime

def getCreated():
    return datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

def connect():
    conn=sqlite3.connect("flask_app/robot/robot.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, message text, created text)")
    cur.execute("CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, log text, created text)")
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, email text, username text, password text, admin INTEGER")
    conn.commit()
    conn.close()

def insert(table, message):
    conn=sqlite3.connect("flask_app/robot/robot.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO " + table + " VALUES (NULL,?,?)",(message,getCreated()))
    conn.commit()
    conn.close()

def view(table):
    conn=sqlite3.connect("flask_app/robot/robot.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM " + table)
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(table, id):
    conn=sqlite3.connect("flask_app/robot/robot.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM " + table + " WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(table, id,message):
    conn=sqlite3.connect("flask_app/robot/robot.db")
    cur=conn.cursor()
    cur.execute("UPDATE " + table + " SET message=? WHERE id=?",(message,id))
    conn.commit()
    conn.close()

connect()
