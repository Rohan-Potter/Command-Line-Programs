#Importing modules
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox
from encryption import ency
from decryption import decy
import mysql.connector
####&&
##### My Sql Connection ####
my_db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="*******",  ## Your Mysql password
    database="login"   ## Database name
)
win=tk.Tk()
win.geometry("1200x1920")
win.title('Practice')
############## login page ################
nb=ttk.Notebook(win)
login_page=ttk.Frame(nb)
nb.add(login_page,text="Login Page")
nb.grid(row=0,column=0)
##########################################
cur=my_db.cursor()
def new():
    win=tk.Tk()
    win.title=("Welcome")
    with open('rohan.txt','r') as f:
        page=f.read()
    message=ttk.Label(win,text=page)
    message.grid(row=0,columnspan=20)
    def close():
        win.destroy()
    close=tk.Button(win,text='Close',command=close)
    close.grid(row=1,column=0,sticky=tk.W)
    close.configure(foreground='Red')

def done():
    key=password_var.get()
    id=login.get()
    query1=f"SELECT * FROM info WHERE login_id='{id}'"
    cur.execute(query1)
    result=cur.fetchone()
    try:
        if result[1]==key:
            new()
        elif result[1]!=key:
            ## Functionality of forget password btn
            def forget():
                win.destroy()
                qin=tk.Tk()
                qin.geometry("1000x1100")
                qin.title("Reset password")
                change_password=ttk.LabelFrame(qin,text='Enter Delails!!')
                change_password.grid(row=0,column=0,padx=450,pady=50)
                #### Forget Password labels
                forget_password_label=ttk.Label(change_password,text='Please! Enter New Password')
                forget_password_label.grid(row=0,column=0,padx=10,pady=15)
                forget_password_var=tk.StringVar()
                forget_password_entry=ttk.Entry(change_password,text=forget_password_var)
                forget_password_entry.grid(row=0,column=1)
                forget_password_entry.focus()
                ##
                forget_password_label_1=ttk.Label(change_password,text='Please! confirm Password')
                forget_password_label_1.grid(row=1,column=0,padx=10,pady=15)
                forget_password_var_1=tk.StringVar()
                forget_password_entry_1=ttk.Entry(change_password,text=forget_password_var_1)
                forget_password_entry_1.grid(row=1,column=1)
               ## confirm btn and functionality
                def changed():
                    new_key=forget_password_var.get()
                    new_key_1=forget_password_var_1.get()
                    if new_key==new_key_1:
                        query2=f"UPDATE info SET password='{new_key}' WHERE login_id='{id}'"
                        cur.execute(query2)
                        my_db.commit()
                        mbox.showinfo("Info","Your password has been Changed")
                        forget_password_entry.delete(0,tk.END)
                        forget_password_entry_1.delete(0,tk.END)
                    else:
                        mbox.showerror('Error','Password Did not match')
                        forget_password_entry.delete(0,tk.END)
                        forget_password_entry_1.delete(0,tk.END)
                confirm_password=tk.Button(change_password,text='Confirm',command=changed)
                confirm_password.grid(row=2,columnspan=2)
                confirm_password.configure(foreground='Red')
                qin.mainloop()
    

            ## Btn             
            forget_password_btn=tk.Button(lable_frame,text="Forget Password",command=forget)
            forget_password_btn.grid(row=3,columnspan=3,padx=40)
            forget_password_btn.configure(foreground="Red")
    except TypeError:
        mbox.showerror("Error","Please Enter Correct Login Id!!")
        login_entry.delete(0,tk.END)
        password_entrybox.delete(0,tk.END)
def redo():
    login_entry.delete(0,tk.END)
    password_entrybox.delete(0,tk.END)
#frame
lable_frame=ttk.LabelFrame(login_page,text='Enter Your Login Details ')
lable_frame.grid(row=0,column=0,padx=550,pady=50)
#Lables and entry box for Id
login=tk.StringVar()
login_id_label=ttk.Label(lable_frame,text='Enter Your Login Id :').grid(row=0,column=0,pady=10)
login_entry=ttk.Entry(lable_frame,text=login)
login_entry.grid(row=0,column=1)
login_entry.focus()
#lable and entery box for password
password_lable=ttk.Label(lable_frame,text='Enter your Password :').grid(row=1,column=0)
password_var=tk.StringVar()
password_entrybox=ttk.Entry(lable_frame,text=password_var)
password_entrybox.grid(row=1,column=1)
#login Button
submit=tk.Button(lable_frame,text='Login',command=done)
submit.grid(row=2,column=0,pady=10)
submit.configure(foreground="Blue")
#Reset Button
reset=tk.Button(lable_frame,text="Reset",command=redo)
reset.grid(row=2,column=1,pady=10)
reset.configure(foreground="blue")
############################################ Forget Password ##################

win.mainloop()
