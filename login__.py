from tkinter import * 
from tkinter import ttk 
from PIL import Image,ImageTk
from logging import NullHandler
from tkinter import messagebox
from home_miniprojek import classroombookingsystem
import sqlite3

class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN")
        self.root.geometry("1550x800+0+0")



        img1=Image.open("C:\\Users\\abdul\\Documents\\GitHub\\miniproject\\UNIMAP.png")
        img1=img1.resize((1550,740),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=740)


        frame1 = Frame(root,bg="white")
        root.config(bg="lightgray")

   


        frame1.place(x=530,y=150,width=500,height=500)
        Label(frame1,text="LOGIN" , font=("times 30 bold"),bg="white",fg="black").place(x=180,y=50)
        Label(frame1,text="Classroom Booking", font=("times 30 bold"),bg="white",fg="black").place(x=80,y=100)

        
        

        #label
        
        id_user = Label(frame1,text="User",font=("times 18 bold"),bg="white",fg="black")
        id_user.place(x=20,y=175)
        pass_user = Label(frame1,text = "Password",font=("times 18 bold"),bg="white",fg="black")
        pass_user.place(x=20,y=250)


        type_val = StringVar()
        id_val = StringVar()
        pass_val = StringVar()

    



        self.pass_box = Entry(frame1,textvariable=pass_val,font=("times 18 bold"),bg="lightgray",fg="black",width=22)
        self.pass_box.place(x=140,y=175)

        self.id_box = Entry(frame1,textvariable=id_val,font=("times 18 bold"),bg="lightgray",fg="black",width=22)
        self.id_box.place(x=140,y=250)

        login=Button(text="Submit",command=self.login,font=("times 16 bold"),bg="red",fg="black").place(x=580,y=505,width=400)


    def login(self):
        if self.id_box.get()=="" or self.pass_box.get()=="":
            messagebox.showerror("Error","Please fill all the fields",parent=self.root)
        

        else:
            conn=sqlite3.connect("login.sqlite")
            my_cursor=conn.cursor()
            my_cursor.execute("CREATE TABLE IF NOT EXISTS login (username TEXT,password TEXT)")
            my_cursor.execute("INSERT INTO login(username,password)VALUES('haziq','211502825')")
            
            my_cursor.execute("SELECT * FROM login where username=? AND password=?",(self.pass_box.get(),self.id_box.get()))                                                                        
            row=my_cursor.fetchone()
            print(self.id_box.get())
            print(row)
            if row==None:
                messagebox.showerror("Error","Invalid Matric Number or Password")
            else:
                self.new_window=Toplevel(self.root)
                self.app=classroombookingsystem(self.new_window)
            conn.commit()
            conn.close
            #print("login succesfull")
            #    messagebox.showinfo("success","next")
            #    self.new_window=Toplevel(self.root)
            #    self.app=classroombookingsystem(self.new_window)



        









if __name__=="__main__":
    root=Tk()
    obj=login_window(root)
    root.mainloop()