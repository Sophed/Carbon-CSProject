#================================================#
#                                                #
#  _________             ___.                    #
#  \_   ___ \_____ ______\_ |__   ____   ____    #
#  /    \  \/\__  \\_  __ \ __ \ /  _ \ /    \   #
#  \     \____/ __ \|  | \/ \_\ (  <_> )   |  \  #
#   \______  (____  /__|  |___  /\____/|___|  /  #
#          \/     \/          \/            \/   #
#                                                #
#================================================#

# A customer details storage system created by (https://github.com/sophed)
# This is a project for my Computer Science class btw I don't know why I would choose to make this lmao

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Colour Palette  -  https://coolors.co/2c363f-e75a7c-f3adbe-ffffff


# === TODO ===
# - Storing data for customers


def presenceCheck(args):
      if args != "":
            return True
      else:
            return False

def init():

      # Main Menu
      def mainMenu():

            # Login Menu
            def loginMenu():

                  # Back Button Functionality
                  def backMain():
                      Lwindow.destroy() # Destroy the previous window.
                      mainMenu()

                  def adminMenu():

                        def addCustomerMenu():
                              
                              #[=============================================]
                              #[              Add Customer Window            ]
                              #[=============================================]

                              def backAdmin():
                                    ACwindow.destroy() # Destroy the previous window.
                                    adminMenu()

                              def saveDetails():

                                    # Check if there is content in the entry boxes
                                    if presenceCheck(usernameEntry.get()) and presenceCheck(passwordEntry.get()):
                                          
                                          with open("customerLogins.txt", mode='a') as loginDatabase: # Open the file
                                                pass # save a combo of the entry fields
                                                
                                    else:
                                          # Show an error if no details are entered
                                          messagebox.showerror("Error", "One or more fields are empty. Please fill all fields.")
                              
                              Awindow.destroy() # Destroy previous window
                              
                              # == Window Config == #
                              ACwindow = tk.Tk()
                              ACwindow.geometry('1000x600')
                              ACwindow.configure(bg='#2C363F')
                              ACwindow.title("Carbon | Add Customer")
                              ACwindow.iconbitmap('icon.ico')

                              # == Frame Config == #
                              ACframe = tk.Frame(
                                    ACwindow,
                                    relief='sunken',
                                    bg="#2C363F"
                              )
                              ACframe.pack(expand= True, padx= 10, pady=20)

                              # == Title Text == #
                              ACmenuText = tk.Label(
                                    ACframe,
                                    text="Add Customer.",
                                    fg="white",
                                    bg="#2C363F",
                                    font=("Arial", 25)
                              ).grid(row=0, column=0)
                              
                              # == Space == #
                              ACmenuText = tk.Label(
                                    ACframe,
                                    text=" ",
                                    bg="#2C363F",
                                    font=("Arial", 16)
                              ).grid(row=1, column=0)
                              
                              # == Name Text == #
                              nameText = tk.Label(
                                    ACframe,
                                    text="Name",
                                    fg="white",
                                    bg="#2C363F",
                                    font=("Arial", 16)
                              ).grid(row=2, column=0)
                              
                              # == Name Entry Field == #
                              nameEntry = tk.Entry(
                                    ACframe,
                                    fg="white",
                                    bg="#F3ADBE",
                                    relief="flat",
                                    font=("Arial", 16),
                                    width=22
                              )
                              nameEntry.grid(row=3, column=0)
                              
                              # == Card Number Text == #
                              cardNumberText = tk.Label(
                                    ACframe,
                                    text="Card Number",
                                    fg="white",
                                    bg="#2C363F",
                                    font=("Arial", 16)
                              ).grid(row=4, column=0)
                              
                              # == Card Number Entry Field == #
                              cardNumberEntry = tk.Entry(
                                    ACframe,
                                    fg="white",
                                    bg="#F3ADBE",
                                    relief="flat",
                                    font=("Arial", 16),
                                    width=22
                              )
                              cardNumberEntry.grid(row=5, column=0)
                              
                              # == ValidFrom Text == #
                              validFromText = tk.Label(
                                    ACframe,
                                    text="Valid From DD/MM/YY",
                                    fg="white",
                                    bg="#2C363F",
                                    font=("Arial", 16)
                              ).grid(row=6, column=0)
                              
                              # == ValidFrom Entry Field == #
                              validFromEntry = tk.Entry(
                                    ACframe,
                                    fg="white",
                                    bg="#F3ADBE",
                                    relief="flat",
                                    font=("Arial", 16),
                                    width=22
                              )
                              validFromEntry.grid(row=7, column=0)
                              
                              # == ValidTo Number Text == #
                              validToText = tk.Label(
                                    ACframe,
                                    text="Valid To DD/MM/YY",
                                    fg="white",
                                    bg="#2C363F",
                                    font=("Arial", 16)
                              ).grid(row=8, column=0)
                              
                              # == ValidTo Entry Field == #
                              validToEntry = tk.Entry(
                                    ACframe,
                                    fg="white",
                                    bg="#F3ADBE",
                                    relief="flat",
                                    font=("Arial", 16),
                                    width=22
                              )
                              validToEntry.grid(row=9, column=0)

                              # == Space == #
                              ACmenuText = tk.Label(
                                    ACframe,
                                    text=" ",
                                    bg="#2C363F",
                                    font=("Arial", 16)
                              ).grid(row=10, column=0)
                              
                              # == Save Button == #
                              ACsaveButton = tk.Button(
                                    ACframe,
                                    text="Save",
                                    width=24,
                                    height=2,
                                    bg="#E75A7C",
                                    fg="white",
                                    font=("Arial", 14),
                                    borderwidth=0,
                                    command=saveDetails
                              ).grid(row=11, column=0)
                              
                              # == Back Button == #
                              ACbackButton = tk.Button(
                                    ACframe,
                                    text="Back",
                                    width=24,
                                    height=2,
                                    bg="#E75A7C",
                                    fg="white",
                                    font=("Arial", 14),
                                    borderwidth=0,
                                    command=backAdmin
                              ).grid(row=12, column=0)
                        
                        #[======================================]
                        #[              Admin Window            ]
                        #[======================================]

                        try:
                              Lwindow.destroy() # Destroy Login Window
                        except:
                              pass
                                    
                        # Back Button Functionality
                        def backLogin():
                            Awindow.destroy() # Destroy the previous window.
                            loginMenu()
                      
                        # == Window Config == #
                        Awindow = tk.Tk()
                        Awindow.geometry('1000x600')
                        Awindow.configure(bg='#2C363F')
                        Awindow.title("Carbon | Admin Menu")
                        Awindow.iconbitmap('icon.ico')

                        # == Frame Config == #
                        Aframe = tk.Frame(
                              Awindow,
                              relief='sunken',
                              bg="#2C363F"
                        )
                        Aframe.pack(expand= True, padx= 10, pady=20)

                        # == Title Text == #
                        AmenuText = tk.Label(
                              Aframe,
                              text="Admin Menu",
                              fg="white",
                              bg="#2C363F",
                              font=("Arial", 25)
                        ).grid(row=0, column=0)

                        # == Space == #
                        AmenuText = tk.Label(
                            Aframe,
                            text=" ",
                            bg="#2C363F",
                            font=("Arial", 16)
                        ).grid(row=1, column=0)
                              
                        # == Add Customer Button == #
                        loginButton = tk.Button(
                              Aframe,
                              text="Add Customer",
                              width=24,
                              height=2,
                              bg="#E75A7C",
                              fg="white",
                              font=("Arial", 14),
                              borderwidth=0,
                              command=addCustomerMenu,
                        ).grid(row=2, column=0)
                        
                        # == Back Button == #
                        exitButton = tk.Button(
                              Aframe,
                              text="Back",
                              width=24,
                              height=2,
                              bg="#E75A7C",
                              fg="white",
                              font=("Arial", 14),
                              borderwidth=0,
                              command=backLogin
                        ).grid(row=3, column=0)
                        

                  #[======================================]
                  #[              Login Window            ]
                  #[======================================]

                  def login():

                        # Check if there is content in the entry boxes
                        if presenceCheck(usernameEntry.get()) and presenceCheck(passwordEntry.get()):
                              
                              with open("logins.txt", mode='r') as loginDatabase: # Open the file
                                    loginsArr = loginDatabase.read().split("\n") # Split the file on line breaks

                              if usernameEntry.get() + ";" + passwordEntry.get() in loginsArr: # Combine the 2 entry fields together and see if it matches the database
                                    adminMenu()
                              else:
                                    # Show an error if the incorrect details are entered
                                    messagebox.showerror("Error", "Incorrect details entered.") 
                                    
                        else:
                              # Show an error if no details are entered
                              messagebox.showerror("Error", "One or more fields are empty. Please enter your login details.")
                  
                  try:
                        Mwindow.destroy() # Destroy the previous window.
                  except:
                        pass # shhh this causes an error when going back from the admin menu but it doesnt actually mess with anything so we can just ignore it
                  
                  # == Window Config == #
                  Lwindow = tk.Tk()
                  Lwindow.geometry('1000x600')
                  Lwindow.configure(bg='#2C363F')
                  Lwindow.title("Carbon | Login")
                  Lwindow.iconbitmap('icon.ico')

                  # == Frame Config == #
                  Lframe = tk.Frame(
                        Lwindow,
                        relief='sunken',
                        bg="#2C363F"
                  )
                  Lframe.pack(expand= True, padx= 10, pady=20)

                  # == Title Text == #
                  LmenuText = tk.Label(
                        Lframe,
                        text="Login.",
                        fg="white",
                        bg="#2C363F",
                        font=("Arial", 25)
                  ).grid(row=0, column=0)
                  
                  # == Space == #
                  LmenuText = tk.Label(
                        Lframe,
                        text=" ",
                        bg="#2C363F",
                        font=("Arial", 16)
                  ).grid(row=1, column=0)
                  
                  # == Username Text == #
                  LmenuText = tk.Label(
                        Lframe,
                        text="Username",
                        fg="white",
                        bg="#2C363F",
                        font=("Arial", 16)
                  ).grid(row=2, column=0)
                  
                  # == Username Entry Field == #
                  usernameEntry = tk.Entry(
                        Lframe,
                        fg="white",
                        bg="#F3ADBE",
                        relief="flat",
                        font=("Arial", 16),
                        width=22
                  )
                  usernameEntry.grid(row=3, column=0)
                  
                  # == Password Text == #
                  LmenuText = tk.Label(
                        Lframe,
                        text="Password",
                        fg="white",
                        bg="#2C363F",
                        font=("Arial", 16)
                  ).grid(row=4, column=0)
                  
                  # == Password Entry Field == #
                  passwordEntry = tk.Entry(
                        Lframe,
                        fg="white",
                        bg="#F3ADBE",
                        relief="flat",
                        font=("Arial", 16),
                        width=22
                  )
                  passwordEntry.grid(row=5, column=0)

                  # == Space == #
                  LmenuText = tk.Label(
                        Lframe,
                        text=" ",
                        bg="#2C363F",
                        font=("Arial", 16)
                  ).grid(row=6, column=0)
                  
                  # == Login Button == #
                  loginButton = tk.Button(
                        Lframe,
                        text="Login",
                        width=24,
                        height=2,
                        bg="#E75A7C",
                        fg="white",
                        font=("Arial", 14),
                        borderwidth=0,
                        command=login
                  ).grid(row=7, column=0)
                  
                  # == Back Button == #
                  backButton = tk.Button(
                        Lframe,
                        text="Back",
                        width=24,
                        height=2,
                        bg="#E75A7C",
                        fg="white",
                        font=("Arial", 14),
                        borderwidth=0,
                        command=backMain
                  ).grid(row=8, column=0)


            #[=================================================]
            #[              Main Startup Window                ]
            #[=================================================]
            
            # == Window Config == #
            Mwindow = tk.Tk()
            Mwindow.geometry('1000x600')
            Mwindow.configure(bg='#2C363F')
            Mwindow.title("Carbon | Main Menu")
            Mwindow.iconbitmap('icon.ico')

            # == Frame Config == #
            Mframe = tk.Frame(
                  Mwindow,
                  relief='sunken',
                  bg="#2C363F"
            )
            Mframe.pack(expand= True, padx= 10, pady=20)

            # == Title Text == #
            MmenuText = tk.Label(
                  Mframe,
                  text="Main Menu",
                  fg="white",
                  bg="#2C363F",
                  font=("Arial", 25)
            ).grid(row=0, column=0)

            # == Space == #
            LmenuText = tk.Label(
                Mframe,
                text=" ",
                bg="#2C363F",
                font=("Arial", 16)
            ).grid(row=1, column=0)
                  
            # == Login Button == #
            loginButton = tk.Button(
                  Mframe,
                  text="Login",
                  width=24,
                  height=2,
                  bg="#E75A7C",
                  fg="white",
                  font=("Arial", 14),
                  borderwidth=0,
                  command=loginMenu,
            ).grid(row=2, column=0)
            
            # == Exit Button == #
            exitButton = tk.Button(
                  Mframe,
                  text="Exit",
                  width=24,
                  height=2,
                  bg="#E75A7C",
                  fg="white",
                  font=("Arial", 14),
                  borderwidth=0,
                  command=exit
            ).grid(row=3, column=0)

      # Start the main menu.
      mainMenu()

# Start the program
init()
