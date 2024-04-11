from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk

# Function to validate user credentials
def validate_login(username, password):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="lucky",
            password="Password123@",
            database="save_user_data",
        )
        cursor = conn.cursor()
        sql = "SELECT * FROM users WHERE username = %s AND password = %s"
        val = (username, password)
        cursor.execute(sql, val)
        user = cursor.fetchone()
        if user:
            messagebox.showinfo('Success', 'Login successful.')
            # You can perform any action after successful login, such as opening a new window.
        else:
            messagebox.showerror('Error', 'Invalid username or password.')
    except mysql.connector.Error as e:
        print(f"Error checking user credentials: {e}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

# Function to handle login button click
def login():
    username = usernameEntry.get()
    password = passwordEntry.get()
    validate_login(username, password)

# GUI setup for login page
login_window = Tk()
login_window.title('Login Page')
login_window.resizable(False,False)
background = ImageTk.PhotoImage(file='bg.jpg')

bgLabel = Label(login_window, image=background)
bgLabel.grid()

Frame = Frame(login_window, bg='white')
Frame.place(x=554, y=100)

heading = Label(Frame, text='LOGIN', font=('Microsoft Yahei UI Light',18,'bold'),
              bg='white', fg='firebrick1')
heading.grid(row=0, column=0, padx=10, pady=10)

usernameLabel = Label(Frame, text='Username', font=('Microsoft Yahei UI Light',10,'bold'), bg='white',
                    fg='firebrick1')
usernameLabel.grid(row=1, column=0, sticky='w', padx=25)

usernameEntry = Entry(Frame, width=30, font=('Microsoft Yahei UI Light',10,'bold'), fg='white', bg='firebrick1')
usernameEntry.grid(row=2, column=0, sticky='w', padx=25)

passwordLabel = Label(Frame, text='Password', font=('Microsoft Yahei UI Light',10,'bold'), bg='white',
                    fg='firebrick1')
passwordLabel.grid(row=3, column=0, sticky='w', padx=25)

passwordEntry = Entry(Frame, width=30, font=('Microsoft Yahei UI Light',10,'bold'), fg='white', bg='firebrick1', show='*')
passwordEntry.grid(row=4, column=0, sticky='w', padx=25)

loginButton = Button(Frame, text='Login', font=('open sansg',16,'bold'), bd=0, bg='firebrick1', fg='white',
                    activebackground='white', activeforeground='firebrick1', width=17, command=login)
loginButton.grid(row=5, column=0, pady=10)

login_window.mainloop()
