from tkinter import *
import tkinter.messagebox

def mainMenu():
    # -- Main Login Window Config
    mainM = Tk()
    mainM.title("Main Menu")
    mainM.geometry("480x400")
    mainM.configure(bg=("#555555"))
    mainM.iconbitmap('icon.ico')

    
def login():

    # Submit Button Functionality
    def submit():
        username = user_entry.get()
        password = pass_entry.get()
        
        if username == "a" and password == "1":
            mainMenu()
            mainLogin.destroy()
        else:
            messagebox.showerror("Error", "Incorrect Details.")
            

    # -- Main Login Window Config
    mainLogin = Tk()
    mainLogin.title("Login Screen")
    mainLogin.geometry("280x100")
    mainLogin.configure(bg=("#555555"))
    mainLogin.iconbitmap('icon.ico')

    # -- Title Text
    Label(
        mainLogin,
        text="Login Menu.",
        borderwidth=0,
        bg="#555555",
        fg="white"
    ).grid(
        columnspan=2,
        row=0,
        sticky="N"
    )

    # -- Username Prompt
    Label(
        mainLogin,
        text="Username:  ",
        borderwidth=0,
        bg="#555555",
        fg="white"
    ).grid(
        column=0,
        row=1,
        sticky="W"
    )

    # -- Username Entry Field
    user_entry = Entry(
        mainLogin,
        width="30",
        borderwidth=0,
        bg="#444444",
        fg="white"
    )
    user_entry.grid(
        column=1,
        row=1,
        sticky="W"
    )
    
    # -- Password Prompt
    Label(
        mainLogin,
        text="Password: ",
        borderwidth=0,
        bg="#555555",
        fg="white"
    ).grid(
        column=0,
        row=2,
        sticky="W"
    )

    # -- Password Entry Field
    pass_entry = Entry(
        mainLogin,
        width="30",
        borderwidth=0,
        bg="#444444",
        fg="white"
    )
    pass_entry.grid(
        column=1,
        row=2,
        sticky="W"
    )
    
    # -- Submit Button
    Button(
        mainLogin,
        text="Submit",
        command=submit,
        borderwidth=0,
        bg="#555555",
        fg="white"
    ).grid(
        columnspan=2,
        row=3,
        sticky="N"
    )

login()
