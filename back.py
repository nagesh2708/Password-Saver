import sqlite3
def connect():
    conn = sqlite3.connect('file.db')
    cur = conn.cursor()
    cur.execute("create table if not exists passwords(id integer primary key,application text,user_id text,password text)")
    conn.commit()
    conn.close()
def view():
    conn = sqlite3.connect('file.db')
    cur = conn.cursor()
    cur.execute("select * from passwords")
    rows = cur.fetchall()
    conn.close()
    return rows
def insert(application,user_id,password):
    conn = sqlite3.connect('file.db')
    cur = conn.cursor()
    cur.execute("insert into passwords values(NULL,?,?,?)",(application,user_id,password))
    conn.commit()
    conn.close()
def delete(id):
    conn = sqlite3.connect('file.db')
    cur = conn.cursor()
    cur.execute("delete from passwords where id=?",(id,))
    conn.commit()
    conn.close()
def deleteall():
    conn = sqlite3.connect('file.db')
    cur = conn.cursor()
    cur.execute("delete from passwords")
    conn.commit()
    conn.close()
def update(id,application,user_id,password):
    conn = sqlite3.connect("file.db")
    cur = conn.cursor()
    cur.execute("update passwords set application=?,user_id=?,password=? where id=?",(application,user_id,password,id))
    conn.commit()
    conn.close()
connect()
