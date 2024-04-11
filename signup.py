from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql
from faker import Faker

def send_verification_code(email):
    fake = Faker()
    verification_code = fake.random_int(min=100000, max=999999)
    # Here, you should implement the functionality to send the verification code to the user's email.
    # For demonstration purposes, I will just print the verification code.
    print(f"Verification code for {email} is {verification_code}")
    return verification_code

def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error','Password Mismatch')
    elif check.get()==0:
        messagebox.showerror('Error','Please accept terms & conditions')
    else:
        verification_code = send_verification_code(emailEntry.get())
        # Here, you should store the user data and the verification code in the database.
        # For demonstration purposes, I will just print the user data and the verification code.
        print(f"Storing user data: username - {usernameEntry.get()}, email - {emailEntry.get()}, password - {passwordEntry.get()}, verification_code - {verification_code}")

def login_page():
    signup_window.destroy()
    import signin

signup_window=Tk()
signup_window.title('Signup Page')
signup_window.resizable(False,False)
background=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(signup_window,image=background)
bgLabel.grid()

Frame=Frame(signup_window,bg='white')
Frame.place(x=554,y=100)

heading=Label(Frame,text='CREATE AN ACCOUNT',font=('Microsoft Yahei UI Light',18,'bold')
              ,bg='white',fg='firebrick1')
heading.grid(row=0,column=0,padx=10,pady=10)


#label 1

usernameLabel=Label(Frame,text='username',font=('Microsoft Yahei UI Light',10,'bold'),bg='white'
                 ,fg='firebrick1')
usernameLabel.grid(row=1,column=0,sticky='w',padx=25)

usernameEntry=Entry(Frame,width=30,font=('Microsoft Yahei UI Light',10,'bold')
              ,fg='white',bg='firebrick1')
usernameEntry.grid(row=2,column=0,sticky='w',padx=25)

#label2

emailLabel=Label(Frame,text='Email',font=('Microsoft Yahei UI Light',10,'bold'),bg='white'
                 ,fg='firebrick1')
emailLabel.grid(row=3,column=0,sticky='w',padx=25)

emailEntry=Entry(Frame,width=30,font=('Microsoft Yahei UI Light',10,'bold')
              ,fg='white',bg='firebrick1')
emailEntry.grid(row=4,column=0,sticky='w',padx=25)

#label 3

passwordLabel=Label(Frame,text='Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white'
                 ,fg='firebrick1')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25)

passwordEntry=Entry(Frame,width=30,font=('Microsoft Yahei UI Light',10,'bold')
              ,fg='white',bg='firebrick1')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

#label 4

confirmLabel=Label(Frame,text='confirm Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white'
                 ,fg='firebrick1')
confirmLabel.grid(row=7,column=0,sticky='w',padx=25)

confirmEntry=Entry(Frame,width=30,font=('Microsoft Yahei UI Light',10,'bold')
              ,fg='white',bg='firebrick1')
confirmEntry.grid(row=8,column=0,sticky='w',padx=25)

check=IntVar()

termsandconditions=Checkbutton(Frame,text='I agree to the terms and conditions',font=('Microsoft Yahei UI Light',9,'bold'),
                               fg='firebrick1',activebackground='white',activeforeground='firebrick1'
                               ,cursor='hand2',variable=check)
termsandconditions.grid(row=9,column=0,pady=10,padx=15)

signupButton=Button(Frame,text='Signup',font=('open sansg',16,'bold'),bd=0,bg='firebrick1',fg='white'
                    ,activebackground='white',activeforeground='firebrick1',width=17, command=connect_database)

signupButton.grid(row=10,column=0,pady=10)

alreadyaccount=Label(Frame,text="Don't have an account?",font=('open sans',9,'bold'),bg='white'
                 ,fg='firebrick1')
alreadyaccount.grid(row=11,column=0,sticky='w',padx=25,pady=10)

loginButton=Button(Frame,text='Log in',font=('open sansg',9,'bold underline')
                   ,bg='white',fg='blue',bd=0,cursor="hand2",activebackground='white'
                   ,activeforeground='blue',command=login_page)
loginButton.grid(row=12,column=0)

signup_window.mainloop()