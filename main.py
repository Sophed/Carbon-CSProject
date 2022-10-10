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


# === [ TODO ] ===

# - Functionality For 
# - GUI For Searching By Card Number
# - ^ Search Customer Details (use card number and provide name, valid from and valid to + list of buissness available)

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

                                    # Check if there is content in the entry boxes and if name contains any ";"
                                    if presenceCheck(nameEntry.get()) and presenceCheck(cardNumberEntry.get()) and presenceCheck(validFromEntry.get()) and presenceCheck(validToEntry.get() and ";" in nameEntry.get()):

                                          # Check if there is "/" in the right places and that text is correct length
                                          if (validFromEntry.get()[2] == "/" and validFromEntry.get()[5] == "/") and (validToEntry.get()[2] == "/" and validToEntry.get()[5] == "/") and len(validFromEntry.get()) == 8 and len(validToEntry.get()) == 8:

                                                # Check to make sure all other characters are numbers
                                                # If you are reading this, I am sorry.
                                                if (validFromEntry.get()[0].isnumeric() and validFromEntry.get()[1].isnumeric() and validFromEntry.get()[3].isnumeric() and validFromEntry.get()[4].isnumeric() and validFromEntry.get()[6].isnumeric() and validFromEntry.get()[7].isnumeric()) and (validToEntry.get()[0].isnumeric() and validToEntry.get()[1].isnumeric() and validToEntry.get()[3].isnumeric() and validToEntry.get()[4].isnumeric() and validToEntry.get()[6].isnumeric() and validToEntry.get()[7].isnumeric()):

                                                      # Check to make sure DD is not bigger than 31 and MM is not bigger than 12
                                                      if (int(validFromEntry.get()[0] + validFromEntry.get()[1]) <= 31) and (int(validFromEntry.get()[3] + validFromEntry.get()[4]) <= 12) and (int(validToEntry.get()[0] + validToEntry.get()[1]) <= 31) and (int(validToEntry.get()[3] + validToEntry.get()[4]) <= 12):
                                                            with open("customerLogins.txt", mode='r') as logins:
                                                                  if cardNumberEntry.get() not in logins.read():
                                                                        if len(cardNumberEntry.get()) == 8 and cardNumberEntry.get()[0] + cardNumberEntry.get()[1] + cardNumberEntry.get()[2] == "SIP" and (cardNumberEntry.get()[3] + cardNumberEntry.get()[4] + cardNumberEntry.get()[5] + cardNumberEntry.get()[6] + cardNumberEntry.get()[7]).isnumeric():
                                                                              with open("customerLogins.txt", mode='a') as loginDatabase:
                                                                                    loginDatabase.write(nameEntry.get() + ";" + cardNumberEntry.get() + ";" + validFromEntry.get() + ";" + validToEntry.get() + "\n")
                                                                                    messagebox.showinfo("Success!", "Details Saved Successfully!")
                                                                        else:
                                                                              messagebox.showerror("Error", "Card is in wrong format.")
                                                                  else:
                                                                        messagebox.showerror("Error", "This card number is in use, please generate a different one.")
                                                      else:
                                                          messagebox.showerror("Error", "Invalid date.")
                                                else:
                                                    messagebox.showerror("Error", "Please use numeric values.")
                                          else:
                                                messagebox.showerror("Error", "Please use the format DD/MM/YY.")
                                                
                                    else:
                                          # Show an error if no details are entered
                                          messagebox.showerror("Error", "One or more fields are empty. Please fill all fields. You also cannot have ';' in a name.")

                              # Generates a new SIP card
                              def generateCard():
                                    if presenceCheck(cardNumberEntry.get()):
                                          messagebox.showerror("Error", "Please remove text before generating a card number.")
                                    else:
                                          cardNumberEntry.insert(0, "SIP" + "00000")
                              
                              Awindow.destroy() # Destroy previous window
                              
                              # == Window Config == #
                              ACwindow = tk.Tk()
                              ACwindow.geometry('500x800')
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
                              
                              # == Generate Button == #
                              ACgenerateButton = tk.Button(
                                    ACframe,
                                    text="Generate Card",
                                    width=24,
                                    height=2,
                                    bg="#E75A7C",
                                    fg="white",
                                    font=("Arial", 14),
                                    borderwidth=0,
                                    command=generateCard
                              ).grid(row=7, column=0)

                              # == Space == #
                              ACmenuText = tk.Label(
                                    ACframe,
                                    text=" ",
                                    bg="#2C363F",
                                    font=("Arial", 16)
                              ).grid(row=8, column=0)
                              
                              # == ValidFrom Text == #
                              validFromText = tk.Label(
                                    ACframe,
                                    text="Valid From DD/MM/YY",
                                    fg="white",
                                    bg="#2C363F",
                                    font=("Arial", 16)
                              ).grid(row=9, column=0)
                              
                              # == ValidFrom Entry Field == #
                              validFromEntry = tk.Entry(
                                    ACframe,
                                    fg="white",
                                    bg="#F3ADBE",
                                    relief="flat",
                                    font=("Arial", 16),
                                    width=22
                              )
                              validFromEntry.grid(row=10, column=0)
                              
                              # == ValidTo Number Text == #
                              validToText = tk.Label(
                                    ACframe,
                                    text="Valid To DD/MM/YY",
                                    fg="white",
                                    bg="#2C363F",
                                    font=("Arial", 16)
                              ).grid(row=11, column=0)
                              
                              # == ValidTo Entry Field == #
                              validToEntry = tk.Entry(
                                    ACframe,
                                    fg="white",
                                    bg="#F3ADBE",
                                    relief="flat",
                                    font=("Arial", 16),
                                    width=22
                              )
                              validToEntry.grid(row=12, column=0)

                              # == Space == #
                              ACmenuText = tk.Label(
                                    ACframe,
                                    text=" ",
                                    bg="#2C363F",
                                    font=("Arial", 16)
                              ).grid(row=13, column=0)
                              
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
                              ).grid(row=14, column=0)
                              
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
                              ).grid(row=15, column=0)

                        def addBusinessMenu():
                              
                              #[=============================================]
                              #[              Add Business Window            ]
                              #[=============================================]

                              def backAdmin():
                                    ABwindow.destroy() # Destroy the previous window.
                                    adminMenu()

                              def saveBDetails():

                                    # Check if there is content in the entry boxes
                                    if presenceCheck(BnameEntry.get()) and presenceCheck(DiscountEntry.get()) and presenceCheck(FreeDelEntry.get()) and presenceCheck(TwoForOneEntry.get()):
                                          
                                          with open("businessDetails.txt", mode='a') as nameDatabase: # Open the file
                                                if (len(BnameEntry.get()) <= 48 and ";" not in BnameEntry.get()): # Length + char check
                                                    if (len(DiscountEntry.get()) == 1 and DiscountEntry.get().isnumeric()): # Length + numeric check
                                                        nameDatabase.write(BnameEntry.get() + ";" + DiscountEntry.get() + ";" + FreeDelEntry.get() + ";" + TwoForOneEntry.get() + "\n")
                                                        messagebox.showinfo("Success!", "Details Saved Successfully!")
                                                    else:
                                                        messagebox.showerror("Error", "Discount day must be a number between 1 and 7")
                                                else:
                                                    messagebox.showerror("Error", "Name must be less than 48 characters and not include ';'")
                                          
                                    else:
                                          # Show an error if no details are entered
                                          messagebox.showerror("Error", "One or more fields are empty. Please fill all fields.")
                              
                              Awindow.destroy() # Destroy previous window
                              
                              # == Window Config == #
                              ABwindow = tk.Tk()
                              ABwindow.geometry('500x800')
                              ABwindow.configure(bg='#2C363F')
                              ABwindow.title("Carbon | Add Business")
                              ABwindow.iconbitmap('icon.ico')

                              # == Frame Config == #
                              ABframe = tk.Frame(
                                    ABwindow,
                                    relief='sunken',
                                    bg="#2C363F"
                              )
                              ABframe.pack(expand= True, padx= 10, pady=20)

                              # == Title Text == #
                              ABmenuText = tk.Label(
                                    ABframe,
                                    text="Add Business.",
                                    fg="white",
                                    bg="#2C363F",
                                    font=("Arial", 25)
                              ).grid(row=0, column=0)
                              
                              # == Space == #
                              ABmenuText = tk.Label(
                                    ABframe,
                                    text=" ",
                                    bg="#2C363F",
                                    font=("Arial", 16)
                              ).grid(row=1, column=0)
                              
                              # == Business Name Text == #
                              BnameText = tk.Label(
                                    ABframe,
                                    text="Name",
                                    fg="white",
                                    bg="#2C363F",
                                    font=("Arial", 16)
                              ).grid(row=2, column=0)
                              
                              # == Business Name Entry Field == #
                              BnameEntry = tk.Entry(
                                    ABframe,
                                    fg="white",
                                    bg="#F3ADBE",
                                    relief="flat",
                                    font=("Arial", 16),
                                    width=22
                              )
                              BnameEntry.grid(row=3, column=0)
                              
                              # == Discount Day Text == #
                              DiscountText = tk.Label(
                                    ABframe,
                                    text="Discount Day 1-7",
                                    fg="white",
                                    bg="#2C363F",
                                    font=("Arial", 16)
                              ).grid(row=4, column=0)
                              
                              # == Discount Day Entry Field == #
                              DiscountEntry = tk.Entry(
                                    ABframe,
                                    fg="white",
                                    bg="#F3ADBE",
                                    relief="flat",
                                    font=("Arial", 16),
                                    width=22
                              )
                              DiscountEntry.grid(row=5, column=0)
                              
                              # == Free Deliveries Text == #
                              FreeDelText = tk.Label(
                                    ABframe,
                                    text="Free Deliveries Y/N",
                                    fg="white",
                                    bg="#2C363F",
                                    font=("Arial", 16)
                              ).grid(row=6, column=0)
                              
                              # == Free Deliveries Entry Field == #
                              FreeDelEntry = tk.Entry(
                                    ABframe,
                                    fg="white",
                                    bg="#F3ADBE",
                                    relief="flat",
                                    font=("Arial", 16),
                                    width=22
                              )
                              FreeDelEntry.grid(row=7, column=0)
                              
                              # == 2 For 1 Product Text == #
                              TwoForOneText = tk.Label(
                                    ABframe,
                                    text="2-For-1 Product",
                                    fg="white",
                                    bg="#2C363F",
                                    font=("Arial", 16)
                              ).grid(row=8, column=0)
                              
                              # == 2 For 1 Product Entry Field == #
                              TwoForOneEntry = tk.Entry(
                                    ABframe,
                                    fg="white",
                                    bg="#F3ADBE",
                                    relief="flat",
                                    font=("Arial", 16),
                                    width=22
                              )
                              TwoForOneEntry.grid(row=9, column=0)

                              # == Space == #
                              ABmenuText = tk.Label(
                                    ABframe,
                                    text=" ",
                                    bg="#2C363F",
                                    font=("Arial", 16)
                              ).grid(row=10, column=0)
                              
                              # == Save Button == #
                              ABsaveButton = tk.Button(
                                    ABframe,
                                    text="Save",
                                    width=24,
                                    height=2,
                                    bg="#E75A7C",
                                    fg="white",
                                    font=("Arial", 14),
                                    borderwidth=0,
                                    command=saveBDetails
                              ).grid(row=11, column=0)
                              
                              # == Back Button == #
                              ABbackButton = tk.Button(
                                    ABframe,
                                    text="Back",
                                    width=24,
                                    height=2,
                                    bg="#E75A7C",
                                    fg="white",
                                    font=("Arial", 14),
                                    borderwidth=0,
                                    command=backAdmin
                              ).grid(row=12, column=0)
                        
                        def viewMenu():
                              
                              #[==============================================]
                              #[              View Customer Window            ]
                              #[==============================================]

                              def backAdmin():
                                    VCwindow.destroy() # Destroy the previous window.
                                    adminMenu()
                              
                              Awindow.destroy() # Destroy previous window
                              
                              # == Window Config == #
                              VCwindow = tk.Tk()
                              VCwindow.geometry('500x800')
                              VCwindow.configure(bg='#2C363F')
                              VCwindow.title("Carbon | View Customer")
                              VCwindow.iconbitmap('icon.ico')

                              # == Frame Config == #
                              VCframe = tk.Frame(
                                    VCwindow,
                                    relief='sunken',
                                    bg="#2C363F"
                              )
                              VCframe.pack(expand= True, padx= 10, pady=20)

                              # == Title Text == #
                              VCmenuText = tk.Label(
                                    VCframe,
                                    text="View Customer Details",
                                    fg="white",
                                    bg="#2C363F",
                                    font=("Arial", 25)
                              ).grid(row=0, column=0)
                              
                              # == Space == #
                              VCspace = tk.Label(
                                    VCframe,
                                    text=" ",
                                    bg="#2C363F",
                                    font=("Arial", 16)
                              ).grid(row=1, column=0)
                              
                              # == TEMPLATE Text == #
                              VCnameText = tk.Label(
                                    VCframe,
                                    text="Sample Text",
                                    fg="white",
                                    bg="#2C363F",
                                    font=("Arial", 16)
                              ).grid(row=2, column=0)
                              
                              # == Back Button == #
                              VCbackButton = tk.Button(
                                    VCframe,
                                    text="Back",
                                    width=24,
                                    height=2,
                                    bg="#E75A7C",
                                    fg="white",
                                    font=("Arial", 14),
                                    borderwidth=0,
                                    command=backAdmin
                              ).grid(row=6, column=0)
                        
                        #[======================================]
                        #[              Admin Window            ]
                        #[======================================]

                        try:
                              Lwindow.destroy() # Destroy Login Window
                        except:
                              pass
                                    
                        # Back Button Functionality
                        def backLogin():
                              if messagebox.askokcancel("Logout", "Confirm Logout?") == True:
                                    Awindow.destroy() # Destroy the previous window.
                                    loginMenu()

                        # == Window Config == #
                        Awindow = tk.Tk()
                        Awindow.geometry('500x800')
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
                        
                        # == Add Business Button == #
                        loginButton = tk.Button(
                              Aframe,
                              text="Add Business",
                              width=24,
                              height=2,
                              bg="#E75A7C",
                              fg="white",
                              font=("Arial", 14),
                              borderwidth=0,
                              command=addBusinessMenu,
                        ).grid(row=3, column=0)
                        
                        # == View Customer Details Button == #
                        viewButton = tk.Button(
                              Aframe,
                              text="View Customer Details",
                              width=24,
                              height=2,
                              bg="#E75A7C",
                              fg="white",
                              font=("Arial", 14),
                              borderwidth=0,
                              command=viewMenu,
                        ).grid(row=4, column=0)
                        
                        # == Logout Button == #
                        exitButton = tk.Button(
                              Aframe,
                              text="Log Out",
                              width=24,
                              height=2,
                              bg="#E75A7C",
                              fg="white",
                              font=("Arial", 14),
                              borderwidth=0,
                              command=backLogin
                        ).grid(row=5, column=0)
                        

                  #[======================================]
                  #[              Login Window            ]
                  #[======================================]

                  def login():

                        
                        #[=============================================]
                        #[              Login Functionality            ]
                        #[=============================================]

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
                        
                        #[=============================================]
                        #[=============================================]
                  
                  try:
                        Mwindow.destroy() # Destroy the previous window.
                  except:
                        pass # shhh this causes an error when going back from the admin menu but it doesnt actually mess with anything so we can just ignore it
                  
                  # == Window Config == #
                  Lwindow = tk.Tk()
                  Lwindow.geometry('500x800')
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
            Mwindow.geometry('500x800')
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
