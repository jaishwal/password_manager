'''
Project - password manager
author - Dheeraj Kumar
'''

from tkinter import *  #built in module
from tkinter import messagebox  # please visit the messagebox doccumentation
from random import choice, randint, shuffle
import pyperclip  #pip install pyperclip

#--------Generating password--------#
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #List comprehension
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)  #take a sequence like a list

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)   # copy and paste clipboard function


#----------save password---------#
def save():
    website = website_entry.get()
    users = email_entry.get()
    password = password_entry.get()

    # condition for checking correction
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {users}"
                                       f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {users} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ------ UI setup---------#
window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)

# labels
website = Label(text="Website:")
website.grid(column=0, row=2)
users = Label(text="Email/Username:")
users.grid(column=0, row=3)
password = Label(text="Password:")
password.grid(column=0, row=4)
#buttons
Gpassword = Button(text="Generate password", command=generate_password)
Gpassword.grid(column=2, row=4)
add = Button(text="Add", width=36, command=save)
add.grid(column=1, row=5, columnspan=2)

#entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=4)

#canvas
canvas = Canvas(width=200, height=189)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 94, image=logo_image)
canvas.grid(column=1, row=0)

window.mainloop() # for when user wants to exit
