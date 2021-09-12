from random import choice, randint, shuffle
from tkinter import messagebox
from tkinter import *
import pyperclip

FONT = "Aria"
LABEL_SIZE = 12
FONT_FAMILY = (FONT, LABEL_SIZE, "normal")
WHITE = "white"

def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="ERROR", message=f"Missing information in your form.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Thes are the details entered: \nEmail: {email} \nPassword: {password} \nOk to save?")
        if is_ok:
            with open("data.txt", mode="a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
                
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

website_label = Label(text="Website:", bg=WHITE)
website_label.grid(column=0, row=1)
website_input = Entry(width=50, border=1)
website_input.grid(column=1, row=1, columnspan=2)

email_label = Label(text="Email/Username:", bg=WHITE)
email_label.grid(column=0, row=2)
email_input = Entry(width=50)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "your-email@gmail.com")

password_label = Label(text="Password:", bg=WHITE)
password_label.grid(column=0, row=3)
password_input = Entry(width=31)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=password_generator)
generate_button.grid(column=2, row=3)

add_button = Button(text="Save", command=save_password, width=43)
add_button.grid(column=1, row=4, columnspan=2)

window.iconbitmap(r'logo.ico')
window.mainloop()