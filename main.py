# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
import pyperclip
from tkinter import *
from tkinter import messagebox


def generate_password():
    letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = list("0123456789")
    symbols = list("!#$%&()*+")

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not website or not email or not password:
        messagebox.showerror(title="Error", message="Please don't leave any fields empty.")
        return

    is_ok = messagebox.askokcancel(
        title=website,
        message=f"Website: {website}\nEmail: {email}\nPassword: {password}\n\nSave these details?"
    )

    if is_ok:
        with open("passwords.txt", "a") as file:
            file.write(f"{website} | {email} | {password}\n")

        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

Label(text="Website").grid(column=0, row=1)
Label(text="Email/Username").grid(column=0, row=2)
Label(text="Password").grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "example@email.com")

password_entry = Entry(width=18)
password_entry.grid(column=1, row=3)

Button(text="Generate Password", command=generate_password).grid(column=2, row=3)
Button(text="Add", width=33, command=save_password).grid(column=1, row=4, columnspan=2)

window.mainloop()
