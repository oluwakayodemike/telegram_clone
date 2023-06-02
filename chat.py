import socket
import threading
import tkinter
from tkinter import simpledialog
from tkinter import font
from tkinter import messagebox
import tkinter.scrolledtext
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

# Server configuration
SERVER = '127.0.0.1'  # Server IP address
PORT = 9090  # Server port number
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"

# Creating a socket client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))


class Client:
    def __init__(self):
        # Initialize the GUI
        self.Window = Tk()
        self.Window.withdraw()

        # Creates the login window
        self.login = Toplevel()
        self.login.title('Sign In')
        self.login.geometry('925x500+300+200')
        self.login.configure(bg='#F5F5F5')
        self.login.resizable(False, False)

        # Load and display the login image
        self.img = PhotoImage(file='login2.png')
        self.label1 = Label(self.login, image=self.img, border=0, bg='#F5F5F5')
        self.label1.place(x=85, y=90)

        # Create the login form
        self.frame = Frame(self.login, width=350, height=350, bg='#F5F5F5')
        self.frame.place(x=470, y=50)

        # Create and place the heading label
        self.heading = Label(self.frame, text='Log In', fg='#57a1f8', bg='#F5F5F5', 
                             font=('Microsoft Yahei UI Light', 23, 'bold'))
        self.heading.place(x=100, y=50)

        # Define event handlers for username entry field
        def on_enter(e):
            self.username.delete(0, 'end')

        def on_leave(e):
            if self.username.get() == '':
                self.username.insert(0, 'Username')

        # Create and place the username entry field
        self.username = Entry(self.frame, width=25, fg='black', border=0, bg='#F5F5F5',
                              font=('Microsoft Yahei UI Light', 11))
        self.username.insert(0, 'Username')
        self.username.bind("<FocusIn>", on_enter)
        self.username.bind("<FocusOut>", on_leave)
        self.username.place(x=30, y=126)

        # Create and place a line for seperation
        self.frame2 = Frame(self.frame, width=295, height=2, bg='black')
        self.frame2.place(x=25, y=150)

        # Defining the event handlers for password text box
        def enter(e):
            self.password.delete(0, 'end')

        def leave(e):
            if self.password.get() == '':
                self.password.insert(0, 'Password')

        # Create and place the password text box
        self.password = Entry(self.frame, width=25, fg='black', border=0, bg='#F5F5F5',
                              font=('Microsoft Yahei UI Light', 11))
        self.password.insert(0, 'Password')
        self.password.bind("<FocusIn>", enter)
        self.password.bind("<FocusOut>", leave)
        self.password.place(x=30, y=180)

        # Create and place another line seperation
        self.frame2 = Frame(self.frame, width=295, height=2, bg='black')
        self.frame2.place(x=25, y=205)

        # Defining a function for the "Remember me" checkbox
        def display():
            if self.x.get() == 1:
                print('Remember User')
            else:
                print("Don't Remember User!")

        # Creating the "Remember me" checkbox
        self.x = IntVar()
        self.check_button = Checkbutton(self.frame, text='Remember me', variable=self.x, onvalue=1, offvalue=2,
                                        command=display, bg='white', fg='black')
        self.check_button.place(x=110, y=230)

        # Creating and adding the "Sign In" button
        self.button = Button(self.frame, width=39, pady=7, text='Sign In', bg='#57a1f8', fg='white', border=0,
                             command=lambda: self.goAhead(self.username.get()))
        self.button.place(x=35, y=265)

        # Creating and placing the tag/label for creating an account
        self.label = Label(self.frame, text='Create an account?', fg='black', bg='white',
                           font=('Microsoft yahei UI Light', 9))
        self.label.place(x=90, y=310)

        # Creating and adding the "Sign Up" button
        self.signup_button = Button(self.frame, width=6, text='Sign Up', border=0, bg='white', cursor='hand2',
                                    fg='#57a1f8', command=lambda: self.goAhead(self.username.get()))
        self.signup_button.place(x=200, y=310)

        # Run the GUI main loop
        self.Window.mainloop()

    def goAhead(self, name):
        # killing the login tab and starting the main chat GUI loop
        self.login.destroy()
        self.gui_loop(name)

        # a thread to receive messages
        rcv = threading.Thread(target=self.receive)
        rcv.start()

    def gui_loop(self, name):
        self.name = name

        # The main chat window configuration
        self.Window.deiconify()
        self.Window.title('Telegram')
        self.Window.geometry('800x590+490+490')
        self.Window.resizable(False, False)
        self.Window.configure(bg="#0e1621")

        # Setting the window icon
        self.icon = PhotoImage(file='logo.png')
        self.Window.iconphoto(True, self.icon)

        # Create and place the text area for displaying messages
        self.text_area = tkinter.scrolledtext.ScrolledText(self.Window, width=64, font=('Open Sans', 10), padx=20, pady=10,
                                                           fg="white", height=60, bg="#121010")
        self.text_area.config(state='disabled')
        self.text_area.place(x=330, y=1)

        # Create and place the sidebar frame
        self.frame = tkinter.Frame(self.Window, width=260, height=589, bg='#17212b')
        self.frame.place(x=70, y=1)

        # Create and place the search bar
        self.search_bar = tkinter.Frame(self.frame, width=240, height=31, bg="#242f3d")
        self.search_bar.place(x=10, y=12)

        # Define event handlers for the search entry field
        def on_enter(e):
            self.search_entry.delete(0, "end")

        def on_leave(e):
            if self.search_entry.get() == '':
                self.search_entry.insert(0, 'Search')

        # Create and placing the search entry field
        self.search_entry = tkinter.Entry(self.search_bar, width=24, border=0, fg="white", font=('Open Sans', 12),
                                          bg="#242f3d")
        self.search_entry.insert(0, "Search")
        self.search_entry.bind("<FocusIn>", on_enter)
        self.search_entry.bind("<FocusOut>", on_leave)
        self.search_entry.place(x=12, y=5)

        # Defining the event handlers for the input space
        def enter(e):
            self.input_area.delete(0, "end")

        def leave(e):
            if self.input_area.get() == '':
                self.input_area.insert(0, 'Write a message...')

        # loading up the image for sending messages.
        self.image = ImageTk.PhotoImage(Image.open('email-send.png'))

        # creating and placing the input area frame
        self.input_area_frame = tkinter.Frame(self.Window, width=469, height=60, bg="#1a1717")
        self.input_area_frame.place(x=331, y=542)

        # input area space
        self.input_area = tkinter.Entry(self.input_area_frame, bg="#2e2a2a", font=('Open Sans', 10), fg="white",
                                        border=0, width=45)
        self.input_area.insert(0, "Your messages..")
        self.input_area.bind("<FocusIn>", enter)
        self.input_area.bind("<FocusOut>", leave)
        self.input_area.place(x=50, y=12)
        self.input_area.focus()

        # send button
        self.send_button = tkinter.Button(self.input_area_frame, image=self.image, border=0, bg="#17212b",
                                          cursor='hand2', command=lambda: self.sendButton(self.input_area.get()))
        self.send_button.place(x=400, y=4)

    def sendButton(self, msg):
        self.text_area.config(state=DISABLED)
        self.msg = msg
        self.input_area.delete(0, END)
        snd = threading.Thread(target=self.sendMessage)
        snd.start()

    def receive(self):
        while True:
            try:
                message = client.recv(1024).decode(FORMAT)

                if message == "NAME":
                    client.send(self.name.encode(FORMAT))
                else:
                    # Enable the text area, insert the received message, and scroll to the end
                    self.text_area.config(state=NORMAL)
                    self.text_area.insert(END, message + "\n\n")
                    print('Receive function running')

                    self.text_area.config(state=DISABLED)
                    self.text_area.see(END)

            except:
                print('Error')
                client.close()
                break

    def sendMessage(self):
        # Disable the text area and send the message
        self.text_area.config(state=DISABLED)
        while True:
            message = (f"{self.name}: {self.msg}")
            client.send(message.encode(FORMAT))
            break


G = Client()
