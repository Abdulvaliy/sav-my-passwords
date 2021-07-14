from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = web_entry.get()
    mail = email_entry.get()
    pswrd = password_entry.get()

    if web == "" or pswrd == "":
        messagebox.showinfo(title="Oops", message="Please, don't leave any fields empty!")   #showinfo  or showerror
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {mail} "
                                                                      f"\nPassword: {pswrd} \n\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{web} | {mail} | {pswrd}\n")
            web_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50,bg="white")
# window.config(minwidth=200, minheight=350)

canvas = Canvas(width=200, height=200,bg="white", highlightthickness=0)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(row=0, column=1)

# LABELS
website = Label(text="Website:", bg="white")
website.grid(row=1, column=0)

email = Label(text="Email/Username:", bg="white")
email.grid(row=2, column=0)

password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)

# ENTRIES
web_entry = Entry(width=41)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

email_entry = Entry(width=41)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "sample@gmail.com")

password_entry = Entry(width=24)
password_entry.grid(row=3, column=1)

# BUTTONS
gen_password = Button(text="Generate Password", command=generate_password, bg="white", padx=2 ,pady=1)
gen_password.grid(row=3, column=2)

add = Button(text="Add", command=save, width=41, bg="white", padx=0 ,pady=4)
add.grid(row=4, column=1, columnspan=2)



window.mainloop()
