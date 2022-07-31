from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox

class cancel_booking:
        def __init__(self,root):
                self.root=root
                self.root.title("Cancel Booking")
                self.root.geometry("1280x550+245+220")

                self.var_matric=StringVar()
                self.var_time=StringVar()
                self.var_user=StringVar()
                self.var_room=StringVar()
                self.var_day=StringVar()
                self.var_date=StringVar()

                lbl_title=Label(self.root,text="Cancel Booking", font=("Comic Sans MS",15, "bold"),bg="white",fg="black",bd=4,relief=FLAT, justify="center", activebackground="grey")
                lbl_title.place(x=-30,y=0,width=1380,height=50)

                lblframeleft=LabelFrame(self.root, text="Cancel Booking :",padx=2,pady=10, font=("Comic Sans MS",30, "bold"),bg="grey",fg="black",bd=2,relief=FLAT)
                lblframeleft.place(x=0,y=60,width=625,height=420)


                #matric
                lbl_id=Label(lblframeleft,padx=4,pady=8,text="Matric Number",font=("Comic Sans MS",20),bg="grey",bd=4)
                lbl_id.grid(row=0,column=0,sticky=W,pady=3)

                id=ttk.Entry(lblframeleft,textvariable=self.var_matric,width=26,font=("Comic Sans MS",15))
                id.grid(row=0,column=1,sticky=W)


                #time slot
                lbl_room_av=Label(lblframeleft,padx=2,pady=8,text="Time Slot",font=("Comic Sans MS",20, ),bg="grey",bd=4)
                lbl_room_av.grid(row=1,column=0,sticky=W)

                combo_room_av=ttk.Combobox(lblframeleft,textvariable=self.var_time,font=("Comic Sans MS",15),width=25,state="read")
                combo_room_av["value"]=("08:00-10:00","10:00-12.00","12:00-14:00","14:00-16:00","16:00-18:00")
                combo_room_av.current()
                combo_room_av.grid(row=1,column=1,sticky=W,pady=3)


                #available room
                lbl_room_av=Label(lblframeleft,padx=2,pady=8,text="Room",font=("Comic Sans MS",20, ),bg="grey",bd=4)
                lbl_room_av.grid(row=2,column=0,sticky=W)

                combo_room_av=ttk.Combobox(lblframeleft,textvariable=self.var_room,font=("Comic Sans MS",15),width=25,state="read")
                combo_room_av["value"]=("BK1","BK2","BK3","BK4","BK5","BK6","BK7","BK8","BK9","BK10","DK1","DK2")
                combo_room_av.current()
                combo_room_av.grid(row=2,column=1,sticky=W,pady=3)


                #user
                lbl_room_av=Label(lblframeleft,padx=2,pady=8,text="User",font=("Comic Sans MS",20, ),bg="grey",bd=4)
                lbl_room_av.grid(row=3,column=0,sticky=W)

                combo_room_av=ttk.Combobox(lblframeleft,textvariable=self.var_user,font=("Comic Sans MS",15),width=25,state="read")
                combo_room_av["value"]=("Student","Lecturer")
                combo_room_av.current()
                combo_room_av.grid(row=3,column=1,sticky=W,pady=3)


                #day
                lbl_day=Label(lblframeleft,padx=2,pady=8,text="Day",font=("Comic Sans MS",20,),bg="grey",bd=4)
                lbl_day.grid(row=4,column=0,sticky=W)

                combo_day=ttk.Combobox(lblframeleft,textvariable=self.var_day,font=("Comic Sans MS",15),width=25,state="read")
                combo_day["value"]=("Monday","Tuesday","Wednesday","Thursday","Friday")
                combo_day.current()
                combo_day.grid(row=4,column=1,sticky=W,pady=3)


                Table_Frame=LabelFrame(self.root,bd=2,relief=FLAT,text="View Details and Search",font=("Comic Sans MS",20),bg="grey",fg="black")
                Table_Frame.place(x=600,y=60,width=720,height=420)

                btn_search=Button(Table_Frame,width=7,bd=4,text="Search By",font=("Comic Sans MS",10),bg="white",fg="black",relief=FLAT, justify="center", activebackground="grey")
                btn_search.grid(row=0,column=0,padx=2,pady=2)


                self.search_var=StringVar()
                combo_search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("Comic Sans MS",15),width=15,state="read")
                combo_search["value"]=("Room")
                combo_search.current()
                combo_search.grid(row=0,column=1,sticky=W,pady=5,padx=2)


                self.txt_search=StringVar()
                txtse=ttk.Entry(Table_Frame,textvariable=self.txt_search,width=20,font=("Comic Sans MS",15))
                txtse.grid(row=0,column=3,sticky=W,pady=5,padx=2)

                btn_show=Button(Table_Frame,width=7,bd=4,command=self.search,text="Show",font=("Comic Sans MS",10),bg="white",fg="black",relief=FLAT, justify="center", activebackground="grey")
                btn_show.grid(row=0,column=5,padx=2,pady=2)

                details_table=Frame(Table_Frame, bd=4,relief=FLAT)
                details_table.place(x=10,y=60,width=650,height=180)


                #scrollbar
                scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)


                self.User_Details_Table=ttk.Treeview(details_table,columns=("matric","time","day","room","user","date"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)

                scroll_x.config(command=self.User_Details_Table.xview)
                scroll_y.config(command=self.User_Details_Table.yview)

                #heading 
                self.User_Details_Table.heading("matric",text="Matric")
                self.User_Details_Table.heading("time",text="Time")
                self.User_Details_Table.heading("user",text="User")
                self.User_Details_Table.heading("room",text="Room")
                self.User_Details_Table.heading("day",text="Day")
                self.User_Details_Table.heading("date",text="Date")

                self.User_Details_Table["show"]="headings"
                self.User_Details_Table.pack(fill=BOTH,expand=1)
                

                #adjust width
                self.User_Details_Table.column("matric",width=100)
                self.User_Details_Table.column("time",width=100)
                self.User_Details_Table.column("day",width=100)
                self.User_Details_Table.column("user",width=100)
                self.User_Details_Table.column("room",width=100)
                self.User_Details_Table.column("date",width=100)
                
                
                self.User_Details_Table.pack(fill=BOTH,expand=1)
                self.User_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
                self.fetch_data()


                btn_frame11= Frame(self.root,bd=2,relief=FLAT,bg="white")
                btn_frame11.place(x=350,y=490,width=300,height=45)


                btncancel=Button(btn_frame11,width=20,command=self.mdelete,text="Delete",font=("Comic Sans MS",14),bg="light gray",fg="black",relief=FLAT, justify="center", activebackground="red")
                btncancel.grid(row=0,column=1,padx=30)

                #exit_btn=Button(btn_frame11,text="Exit",command=self.exit,width=20,font=("Comic Sans MS",15),bg="light gray",fg="black",bd=4,relief=FLAT, justify="center", activebackground="red")
                #exit_btn.grid(row=0,column=1,padx=50)


        def mdelete(self):
                mdelete=messagebox.askyesno("Delete","Do you want to cancel this Booking",parent=self.root)
                if mdelete>0:
                        conn=sqlite3.connect("login.sqlite")
                        my_cursor=conn.cursor()
                        query="delete from booking1 where matric =?"
                        value=(self.var_matric.get(),)
                        my_cursor.execute(query,value)
                else:
                        if not mdelete:
                                        return
                conn.commit()
                self.fetch_data()
                conn.close()


        def fetch_data(self):
                conn=sqlite3.connect("login.sqlite")
                my_cursor=conn.cursor()
                my_cursor.execute("CREATE TABLE IF NOT EXISTS booking1 (matric TEXT ,time TEXT,day TEXT, room TEXT,user TEXT,date TEXT)")
                my_cursor.execute("select * from booking1")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                        self.User_Details_Table.delete(*self.User_Details_Table.get_children())
                        for i in rows:
                                self.User_Details_Table.insert("",END,values=i)
                conn.commit()
                conn.close()


        def get_cursor(self,matric= ""):
                cursor_row=self.User_Details_Table.focus()
                content=self.User_Details_Table.item(cursor_row)
                row=content["values"]

                self.var_matric.set(row[0]),
                self.var_time.set(row[1]),
                self.var_day.set(row[2]),
                self.var_room.set(row[3]),
                self.var_user.set(row[4])

        def search(self):
                conn=sqlite3.connect("login.sqlite")
                my_cursor=conn.cursor()
                my_cursor.execute
                my_cursor.execute("select * from booking1 where "+ str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                        self.User_Details_Table.delete(*self.User_Details_Table.get_children())
                        for i in rows:
                                self.User_Details_Table.insert("",END,values=i)
                                print(i)
                        conn.commit()
                conn.close()


        def exit(self):
                self.root.destroy()


if __name__ == "__main__":
    root=Tk()
    obj=cancel_booking(root)
    root.mainloop()