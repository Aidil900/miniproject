from tkinter import * 
from PIL import Image,ImageTk
from room_ import room_booking
from cancel import cancel_booking



class classroombookingsystem:
        def __init__(self,root):
                self.root=root
                self.root.title("Classroom Booking System")
                self.root.geometry("1550x800+0+0")
                
    
#================= 1st Image============#
                img1=Image.open("UNIMAP.png")
                img1=img1.resize((1550,240),Image.ANTIALIAS)
                self.photoimg1=ImageTk.PhotoImage(img1)

                lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
                lblimg.place(x=0,y=0,width=1550,height=240)


#================= 2nd Image============#
                img2=Image.open("uni.png")
                img2=img2.resize((220,180),Image.ANTIALIAS)
                self.photoimg2=ImageTk.PhotoImage(img2)

                lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
                lblimg.place(x=0,y=0,width=242,height=200)
        
#================= Title============#
                lbl_title=Label(self.root,text=" ClassRoom Booking System", font=("times new roman",30,"bold"),bg="black",fg="orange",bd=4,relief=RIDGE)
                lbl_title.place(x=240,y=140,width=1300,height=50)

#============= main frame============#
                main_frame=Frame(self.root,bd=4,relief=RIDGE)
                main_frame.place(x=0,y=190,width=1550,height=620)

#=========== home ========#
                lbl_menu=Label(main_frame,text="Portal", font=("Sans serif",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
                lbl_menu.place(x=0,y=0,width=240,height=55)

                lbl_frame=Frame(main_frame,bd=0,relief=RIDGE)
                lbl_frame.place(x=0,y=50,width=240,height=370)

#========= button Frame=======#

                #user_btn=Button(lbl_frame,text="User Details",command=self.user_details,width=22,font=("Comic Sans MS",15, "bold"),bg="white",fg="black",bd=4,relief=FLAT, justify="center", activebackground="grey")
                #user_btn.grid(row=0,column=0,pady=1)

                rm_btn=Button(lbl_frame,text="Book Room",command=self.room_details,width=22,font=("Comic Sans MS",15, "bold"),bg="white",fg="black",bd=4,relief=FLAT, justify="center", activebackground="grey")
                rm_btn.grid(row=1,column=0,pady=1,padx=0)

                #v_btn=Button(lbl_frame,text="Booking Details",command=self.view_booking,width=22,font=("Comic Sans MS",15, "bold"),bg="white",fg="black",bd=4,relief=FLAT, justify="center", activebackground="grey")
                #v_btn.grid(row=2,column=0,pady=1)

                cancel_btn=Button(lbl_frame,text="Cancel Booking",command=self.cancel_booking,width=22,font=("Comic Sans MS",15, "bold"),bg="white",fg="black",bd=4,relief=FLAT, justify="center", activebackground="grey")
                cancel_btn.grid(row=3,column=0,pady=1)

                logout_btn=Button(lbl_frame,text="Exit",command=self.exit,width=22,font=("Comic Sans MS",15, "bold"),bg="white",fg="black",bd=4,relief=FLAT, justify="center", activebackground="red")
                logout_btn.grid(row=4,column=0,pady=1)


#========== 3rd image=====#
                img3=Image.open("whitebg.jpg")
                img3=img3.resize((1450,600),Image.ANTIALIAS)
                self.photoimg3=ImageTk.PhotoImage(img3)

        
                lblimg=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
                lblimg.place(x=240,y=190,width=1290,height=610)

                
        #def user_details(self):
        #   self.new_window= Toplevel(self.root) 
        #   self.app=user_window(self.new_window) 

        def room_details(self):
                self.new_window= Toplevel(self.root) 
                self.app=room_booking(self.new_window) 
       

        def cancel_booking(self):
                self.new_window=Toplevel(self.root)
                self.app=cancel_booking(self.new_window)

        def exit(self):
                self.root.destroy()
           

if __name__ == "__main__":
        root=Tk()
        obj=classroombookingsystem(root)
        root.mainloop()