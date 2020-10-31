from tkinter import *
import sqlite3
import back
from tkinter import messagebox
root = Tk()
def superuser():
    conn = sqlite3.connect("file.db")
    cur = conn.cursor()
    cur.execute("create table if not exists admin(key text primary key)")
    cur.execute("select * from admin")
    global val
    val = cur.fetchall()
    conn.commit()
    if(len(val)==0):
        cur.execute("insert into admin values('nag')")
        cur.execute("select * from admin")
        val = cur.fetchall()
        conn.commit()
    conn.close()
superuser()

def showpasswords():
    root = Tk()
    def viewall():
        list1.delete(0,END)
        for i in back.view():
            list1.insert(END,i)
    def get_selected_row(event):
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
    def add_db():
        if(e1.get()!='' and e2.get()!='' and e3.get()!=''):
            back.insert(e1.get(),e2.get(),e3.get())
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
        else:
            messagebox.showerror("Error","Empty values cannot be added")
        viewall()
    def del_db():
        if(e1.get()!='' and e2.get()!='' and e3.get()!=''):
            back.delete(selected_tuple[0])
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
        else:
            messagebox.showerror("Error","Empty values cannot be deleted")
        viewall()
    def update_db():
        if(e1.get()!='' and e2.get()!='' and e3.get()!=''):
            back.update(selected_tuple[0],e1.get(),e2.get(),e3.get())
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
        else:
            messagebox.showerror("Error","Empty values cannot be updated")
        viewall()
    def dall_db():
        back.deleteall()
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        viewall()
    l1 = Label(root,text="Application")
    l1.place(x=10,y=10)
    l2 = Label(root,text="User Name")
    l2.place(x=10,y=40)
    l3 = Label(root,text="Password")
    l3.place(x=10,y=70)
    e1 = Entry(root)
    e1.place(x=80,y=10)
    e2 = Entry(root)
    e2.place(x=80,y=40)
    e3 = Entry(root)
    e3.place(x=80,y=70)
    root.title("Passwords")
    b1 = Button(root,text="add",width=6,command=add_db)
    b1.place(x=10,y=100)
    b2 = Button(root,text="delete",width=6,command=del_db)
    b2.place(x=70,y=100)
    b3 = Button(root,text="update",width=6,command=update_db)
    b3.place(x=130,y=100)
    b4 = Button(root,text="delete all",width=6,command=dall_db)
    b4.place(x=190,y=100)
    list1 = Listbox(root,height=6,width=35)
    list1.place(x=10,y=130)
    sb1 = Scrollbar(root)
    sb1.place(x=220,y=130)
    list1.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list1.yview)
    list1.bind("<<ListboxSelect>>",get_selected_row)
    root.geometry("300x300+100+100")
    viewall()
    root.mainloop()
def validate():
    global val
    x = e1.get()
    if(x==val[0][0]):
        root.destroy()
        showpasswords()
    else:
        messagebox.showerror("Error","Password Incorrect")
def reset():
    root1 = Tk()
    def xyz():
        global val
        a1 = e1.get()
        a2 = e2.get()
        if(a1=='' or a2==''):
            messagebox.showerror("Error","Password fields cannot not be empty")
            root1.destroy()
        elif(a1==a2):
            conn = sqlite3.connect("file.db")
            cur = conn.cursor()
            cur.execute("update admin set key=? where key=?",(a1,val[0][0]))
            conn.commit()
            cur.execute("select * from admin")
            val = cur.fetchall()
            conn.commit()
            conn.close()
            root1.destroy()
        else:
            messagebox.showerror("Error","Password fields doesnot match")
            root1.destroy()
    l1 = Label(root1,text="New Password")
    l1.place(x=10,y=10)
    l2 = Label(root1,text="New Password")
    l2.place(x=10,y=40)
    e1 = Entry(root1)
    e1.place(x=100,y=10)
    e2 = Entry(root1)
    e2.place(x=100,y=40)
    b1 = Button(root1,text='submit',command=xyz)
    b1.place(x=40,y=70)
    root1.geometry("250x100+50+50")
    root1.mainloop()

l1 = Label(root,text="Password:")
l1.place(x=10,y=10)
e1 = Entry(root)
e1.place(x=70,y=10)
b1 = Button(root,text="Submit",command=validate)
b1.place(x=60,y=40)
b2 = Button(root,text="Reset Password",command=reset)
b2.place(x=40,y=70)
root.title("Login Page")
root.geometry("220x120+50+50")
root.mainloop()
