from tkinter import * 
from PIL import Image,ImageTk
from tkinter import messagebox
from home_miniprojek import classroombookingsystem
import sqlite3
from PIL import Image,ImageTk
from tkinter import ttk


def main():
    win=Tk()
    obj=login_window(win)
    win.mainloop()



#===============================================
class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN")
        self.root.geometry("1550x800+0+0")

#=======image in login window
        img1=Image.open("UNIMAP.jpg")
        img1=img1.resize((1550,740),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

#label img1
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=740)     

#frame login
        frame1 = Frame(root,bg="white")
        root.config(bg="lightgray")

        frame1.place(x=530,y=150,width=500,height=500)
        Label(frame1,text="LOGIN" , font=("times 30 bold"),bg="white",fg="black").place(x=180,y=50)
        Label(frame1,text="Classroom Booking", font=("times 30 bold"),bg="white",fg="black").place(x=80,y=100)

#label in frame1
        id_user = Label(frame1,text="User",font=("times 18 bold"),bg="white",fg="black")
        id_user.place(x=20,y=175)
        pass_user = Label(frame1,text = "Password",font=("times 18 bold"),bg="white",fg="black")
        pass_user.place(x=20,y=250)


#variable        
        user_val = StringVar()
        password_val = StringVar()

    


#box entry
        self.password_box = Entry(frame1,textvariable=password_val,font=("times 18 bold"),bg="lightgray",fg="black",width=22)
        self.password_box.place(x=140,y=175)

        self.user_box = Entry(frame1,textvariable=user_val,font=("times 18 bold"),bg="lightgray",fg="black",width=22)
        self.user_box.place(x=140,y=250)
#button login

        btn_frames= Frame(self.root,bd=2,relief=FLAT,bg="white")
        btn_frames.place(x=670,y=490,width=200,height=50)

        login=Button(btn_frames,text="Submit",command=self.login,font=("times 16 bold"),bg="light gray",fg="black",activeforeground="white",activebackground="red")
        login.grid(row=0,column=0,padx=55,pady=0)

#button register
       # btn_frames2=Frame(self.root, bd=2, relief=FLAT, bg='grey')
       # btn_frames2.place(x=680,y=560,width=190,height=40)

        regis=Button(text="New User Register",command=self.register,font=("times 15 bold"),borderwidth=0,bg="light grey",fg="black",activeforeground="white",activebackground="light blue")
        #regis.grid(row=2,column=0,padx=5,pady=0)
        regis.place(x=680,y=560,width=190,height=40)
    


#database login 
    def login(self):
        if self.user_box.get()=="" or self.password_box.get()=="":
            messagebox.showerror("Error","Please fill all the fields",parent=self.root)

        elif self.user_box.get()=="admin" and self.password_box.get()=="123456":
            messagebox.showinfo("Hello","Hello Registered User")

        else:
            conn=sqlite3.connect("login.sqlite")
            my_cursor=conn.cursor()
            my_cursor.execute("CREATE TABLE IF NOT EXISTS login (username TEXT,password TEXT)")
            #my_cursor.execute("INSERT INTO login(username,password)VALUES('admin','123456')")
            

            my_cursor.execute("SELECT * FROM login where username=? AND password=?",(self.password_box.get(),self.user_box.get()))                                                                        
            row=my_cursor.fetchone()
            print(self.user_box.get())
            print(row)
            if row==None:
                messagebox.showerror("Error","Invalid Username or Password")
            else:
                
                messagebox.showinfo("Success","Welcome To Portal")
                self.new_window=Toplevel(self.root)
                self.app=classroombookingsystem(self.new_window)
            conn.commit()
            conn.close


#====function open window register
    def register(self):
            self.new_window=(self.root) 
            self.app=register_room(self.new_window)
            

#======= window register
class register_room:
    
    def __init__(self,root):
            self.root=root
            self.root.title("Register")
            self.root.geometry("1200x500+150+150")

            img1=Image.open("UNIMAP.jpg")
            img1=img1.resize((1200,500),Image.ANTIALIAS)
            self.photoimg1=ImageTk.PhotoImage(img1)

            lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
            lblimg.place(x=0,y=0,width=1200,height=500)


            img2=Image.open("whitebg.jpg")
            img=img2.resize((1200,500),Image.ANTIALIAS)
            self.photoimg2=ImageTk.PhotoImage(img2)

            lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
            lblimg.place(x=350,y=150,width=500,height=200)


#frame username,pass,confirm
            frame1=Frame(self.root,bg="lightgrey")
            frame1.place(x=350,y=150,width=498,height=200)
            #self.root.config(bg="lightgray")

#label in frame1            
            Label(frame1,text="Username" , font=("times 15 bold"),bg="light gray",fg="black").place(x=20,y=50)
            Label(frame1,text="Password", font=("times 15 bold"),bg="light gray",fg="black").place(x=20,y=80)
            Label(frame1,text="Confirm Password", font=("times 15 bold"),bg="light gray",fg="black").place(x=20,y=110)

            Label(frame1,text="REGISTER HERE", font=("times 20 bold"),bg="light gray",fg="black").place(x=120,y=10)


#============variable=============#
            user_val = StringVar()
            password_val = StringVar()
            confirmpass_val = StringVar()

#==========box text entry
            self.user_box = ttk.Entry(frame1,textvariable=user_val,font=("times 15 bold"),width=20)
            self.user_box.place(x=180,y=50)
            
            self.password_box = ttk.Entry(frame1,textvariable=password_val,font=("times 15 bold"),width=20)
            self.password_box.place(x=180,y=80)
            
            self.confirm_box =ttk.Entry(frame1,textvariable=confirmpass_val,font=("times 15 bold"),width=20)
            self.confirm_box.place(x=180,y=110)


            regis=Button(text="Register",font=("times 15 bold"),command=self.add_user,bg="light grey",fg="black",activeforeground="white",activebackground="light blue")
            regis.place(x=540,y=300,width=120,height=20)


#========function add new user
    def add_user(self):
            if self.user_box.get()=="" or self.password_box.get()=="" or self.confirm_box.get()=="":
                messagebox.showerror("Error","Please fill all the fields",parent=self.root)
            
            elif self.password_box.get() != self.confirm_box.get():
                messagebox.showerror("Error","Password & confirm password must be same")

            else:

                u=self.user_box.get()
                p=self.password_box.get()
                c=self.confirm_box.get()

                conn=sqlite3.connect("login.sqlite")
                my_cursor=conn.cursor()
                my_cursor.execute("CREATE TABLE IF NOT EXISTS login (username TEXT,password TEXT)")
                my_cursor.execute("SELECT * FROM login where username=? AND password=? ",(self.user_box.get(),self.password_box.get()))                                                                        
                row=my_cursor.fetchone()
                print(self.user_box.get())
                print(row)
                if row!=None:
                    messagebox.showerror("Error"," username already exist")
                else:
                    open_main=messagebox.askyesno("yesno","Please add user details")
                    
                    my_cursor.execute("INSERT INTO login(username,password)VALUES(?,?)",(u,p))
                
    
                conn.commit()
                conn.close 

#==========function open user_window in user
                self.new_window=Toplevel(self.root)
                self.app=user_window(self.new_window)



#==================================================================================


class user_window:
        def __init__(self,root):
                self.root=root
                self.root.title("Users Details")
                self.root.geometry("1280x550+150+200")




#==================variables for database==============#
                self.var_utype=StringVar()
                self.var_uname=StringVar()
                self.var_uemail=StringVar()
                self.var_ugender=StringVar()
                self.var_uid=StringVar()



#======================== title =======================#
                lbl_title=Label(self.root,text="ADD User Details", font=("Comic Sans MS",15, "bold"),bg="white",fg="black",bd=4,relief=FLAT, justify="center", activebackground="grey")
                lbl_title.place(x=-30,y=0,width=1380,height=50)
        

                lblframeleft=LabelFrame(self.root, text=" User Details :",padx=2,pady=10, font=("Comic Sans MS",20, "bold"),bg="grey",fg="black",bd=2,relief=FLAT)
                lblframeleft.place(x=10,y=60,width=425,height=450)


#======================label and entry=================#
        #in user detail
        #user type

                lbl_user_type=Label(lblframeleft,padx=2,pady=10,text="User Type",font=("Comic Sans MS",15, ),bg="grey",bd=4)
                lbl_user_type.grid(row=0,column=0,sticky=W)

                combo_user=ttk.Combobox(lblframeleft,textvariable=self.var_utype,font=("Comic Sans MS",15),width=19,state="read")
                combo_user["value"]=("Lecturer","Student")
                combo_user.current()
                combo_user.grid(row=0,column=1,sticky=W,pady=3)

        #User id type
                lbl_user_id=Label(lblframeleft,padx=2,pady=10,text="Matric Number",font=("Comic Sans MS",15),bg="grey",bd=4)
                lbl_user_id.grid(row=1,column=0,sticky=W,pady=3)

                txtid=ttk.Entry(lblframeleft,textvariable=self.var_uid,width=20,font=("Comic Sans MS",15))
                txtid.grid(row=1,column=1)

        #user name
                lbl_user_name=Label(lblframeleft,padx=2,pady=10,text="Name",font=("Comic Sans MS",15),bg="grey",bd=4)
                lbl_user_name.grid(row=2,column=0,sticky=W,pady=3)

                txtuname=ttk.Entry(lblframeleft,textvariable=self.var_uname,width=20,font=("Comic Sans MS",15))
                txtuname.grid(row=2,column=1)

        #email     
                lbl_email=Label(lblframeleft,padx=2,pady=10,text="Email ",font=("Comic Sans MS",15),bg="grey",bd=4)
                lbl_email.grid(row=3,column=0,sticky=W,pady=3)

                email=ttk.Entry(lblframeleft,textvariable=self.var_uemail,width=20,font=("Comic Sans MS",15))
                email.grid(row=3,column=1)

        #gender
                lbl_gender=Label(lblframeleft,padx=2,pady=10,text="Gender",font=("Comic Sans MS",15),bg="grey",bd=4)
                lbl_gender.grid(row=4,column=0,sticky=W,pady=3)

                combo_gender=ttk.Combobox(lblframeleft,textvariable=self.var_ugender,font=("Comic Sans MS",15),width=19,state="read")
                combo_gender["value"]=("Male","Female")
                combo_gender.current()
                combo_gender.grid(row=4,column=1,sticky=W,pady=3)

        #button in frame user detail
                btn_frame1= Frame(lblframeleft,bd=2,relief=FLAT,bg="grey")
                btn_frame1.place(x=-10,y=330,width=460,height=50)


                btnAdd=Button(btn_frame1,command=self.add_data,width=7,text="Add",font=("Comic Sans MS",15),bg="white",fg="black",relief=FLAT, justify="center", activebackground="grey")
                btnAdd.grid(row=0,column=0,padx=5)

                btn_update=Button(btn_frame1,command=self.update,width=7,text="Update",font=("Comic Sans MS",15),bg="white",fg="black",relief=FLAT, justify="center", activebackground="grey")
                btn_update.grid(row=0,column=1,padx=5)

                btn_delete=Button(btn_frame1,command=self.mdelete,width=7,text="Delete",font=("Comic Sans MS",15),bg="white",fg="black",relief=FLAT, justify="center", activebackground="grey")
                btn_delete.grid(row=0,column=2,padx=5)

                btn_rese=Button(btn_frame1,command=self.reset,width=7,text="Reset",font=("Comic Sans MS",15),bg="white",fg="black",relief=FLAT, justify="center", activebackground="grey")
                btn_rese.grid(row=0,column=3,padx=5)

                btn_next=Button(self.root,command=self.home,width=7,text="Next",font=("Comic Sans MS",18),bg="maroon",fg="white",relief=FLAT, justify="center", activebackground="grey")
                btn_next.grid(row=7,column=5,padx=500,pady=500)


        #========== Frame search =========#
               
                Table_Frame=LabelFrame(self.root,bd=2,relief=FLAT,text="View Details and Search",font=("Comic Sans MS",20),bg="grey",fg="black")
                Table_Frame.place(x=428,y=60,width=725,height=450)

        #in view detail and search
        #search by button  
                btn_search=Button(Table_Frame,width=7,bd=4,text="Search By",font=("Comic Sans MS",10),bg="white",fg="black",relief=FLAT, justify="center", activebackground="grey")
                btn_search.grid(row=0,column=0,padx=2,pady=2)

                self.search_var=StringVar()
                combo_search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("Comic Sans MS",15),width=15,state="read")
                combo_search["value"]=("Name","Matric ")
                combo_search.current()
                combo_search.grid(row=0,column=1,sticky=W,pady=5,padx=2)


                self.txt_search=StringVar()
                txtse=ttk.Entry(Table_Frame,textvariable=self.txt_search,width=20,font=("Comic Sans MS",15))
                txtse.grid(row=0,column=3,sticky=W,pady=5,padx=2)

                btnsearch=Button(Table_Frame,command=self.search,width=7,bd=4,text="Search",font=("Comic Sans MS",10),bg="white",fg="black",relief=FLAT, justify="center", activebackground="grey")
                btnsearch.grid(row=0,column=4,padx=2,pady=2)

                btn_show=Button(Table_Frame,command=self.fetch_data,width=7,bd=4,text="Show all",font=("Comic Sans MS",10),bg="white",fg="black",relief=FLAT, justify="center", activebackground="grey")
                btn_show.grid(row=0,column=5,padx=2,pady=2)


        #======== show data table==========#
                details_table=Frame(Table_Frame, bd=4,relief=FLAT)
                details_table.place(x=10,y=60,width=650,height=300)


        #scrollbar
                scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        #table
                self.Details=(ttk.Treeview(details_table,columns=("user","name","email","gender","matric")))#(xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)

                scroll_x.config(command=self.Details.xview)
                scroll_y.config(command=self.Details.yview)

        #heading treeview view detail and search 
                self.Details.heading("user",text="User")
                self.Details.heading("name",text="Name")
                self.Details.heading("email",text="Email")
                self.Details.heading("matric",text="Matric")
                self.Details.heading("gender",text="Gender")

                self.Details["show"]="headings"
                self.Details.pack(fill=BOTH,expand=1)
                
        #adjust width heading
                self.Details.column("user",width=100)
                self.Details.column("name",width=100)
                self.Details.column("email",width=200)
                self.Details.column("matric",width=100)
                self.Details.column("gender",width=100)

                self.Details.pack(fill=BOTH,expand=1)
                self.Details.bind("<ButtonRelease-1>",self.get_cursor)
                self.fetch_data()

        #database add data in user detail
        def add_data(self):
                if self.var_uid.get()=="" or self.var_uname.get()=="" or self.var_uemail.get()=="":
                        messagebox.showerror("Error","Please Fill All the Details")
                else:
                        try:
                
                                conn=sqlite3.connect("login.sqlite")
                                u=self.var_utype.get()
                                nm=self.var_uname.get()
                                em=self.var_uemail.get()
                                g=self.var_ugender.get()
                                i=self.var_uid.get()

                                

                                my_cursor=conn.cursor()
                                my_cursor.execute("CREATE TABLE IF NOT EXISTS userinfo1 (user TEXT unique,name TEXT,email TEXT,gender TEXT,matric INTEGER)")
                                #my_cursor.execute("INSERT INTO userinfo1 (user,Name,email,Gender,Matric)VALUES(?,?,?,?,?)",(u,nm,em,g,i))
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("Success","User Added",parent=self.root)
                        except Exception as es:
                                messagebox.showwarning("Warning",f"Something went Wrong:{str(es)}",parent=self.root)


        def fetch_data(self):
                conn=sqlite3.connect("login.sqlite")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from userinfo1")
                rows=my_cursor.fetchall()
                print(rows)
                if len(rows)!=0:
                        self.Details.delete(*self.Details.get_children())
                        for i in rows:
                                self.Details.insert("",END,values=i)
                                print(i)
                        conn.commit()
                        conn.close()

        def get_cursor(self,matric= ""):
                cursor_row=self.Details.focus()
                content=self.Details.item(cursor_row)
                row=content["values"]

                self.var_utype.set(row[0]),
                self.var_uname.set(row[1]),
                self.var_uemail.set(row[2]),
                self.var_ugender.set(row[3]),
                self.var_uid.set(row[4])



        def update(self):
                if self.var_uid.get()=="":
                        messagebox.showerror("Error","Please fil the field before click add or update",parent=self.root)
                else:

                        u=self.var_utype.get()
                        nm=self.var_uname.get()
                        em=self.var_uemail.get()
                        g=self.var_ugender.get()
                        i=self.var_uid.get()


                        conn=sqlite3.connect("login.sqlite")
                        my_cursor=conn.cursor()
                        my_cursor.execute("INSERT INTO userinfo1 (user,Name,email,Gender,Matric)VALUES(?,?,?,?,?)",(u,nm,em,g,i))
                        #my_cursor.execute("INSERT INTO userinfo1 SET user=?,Name=?,email=?,Gender=? WHERE Matric=?",(
                                                                                        #self.var_utype.get(),
                                                                                        #self.var_uname.get(),
                                                                                        #self.var_uemail.get(),
                                                                                        #self.var_ugender.get(),
                                                                                        #self.var_uid.get()
                                                                                        #))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Updated","User Details has been Updated Successully",parent=self.root)
                                       
        def mdelete(self):
                mdelete=messagebox.askyesno("Delete","Do you want to delete this User",parent=self.root)
                if mdelete>0:
                        conn=sqlite3.connect("login.sqlite")
                        my_cursor=conn.cursor()
                        query="delete from userinfo1 where Name =?"
                        value=(self.var_uname.get(),)
                        my_cursor.execute(query,value)
                else:
                        if not mdelete:
                                        return
                conn.commit()
                self.fetch_data()
                conn.close()

        def reset(self,matric=""):
                cursor_row=self.Details.focus()
                content=self.Details.item(cursor_row)
                row=content["values"]

                self.var_utype.set(""),
                self.var_uid.set(""),
                self.var_uname.set(""),
                self.var_uemail.set(""),
                self.var_ugender.set("")

        def search(self):
                conn=sqlite3.connect("login.sqlite")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from userinfo1 where "+ str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                        self.Details.delete(*self.Details.get_children())
                        for i in rows:
                                self.Details.insert("",END,values=i)

                conn.commit()
                conn.close()
        

        def home(self):
                messagebox.showinfo("Success","Please Login with new username and password")
                self.new_window=Toplevel(self.root)
                self.app=login_window(self.new_window)
                
    


if __name__=="__main__":
    main()