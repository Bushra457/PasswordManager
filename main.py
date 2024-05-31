import tkinter
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)
    input_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = input_web.get()
    mail = input_mail.get()
    password = input_password.get()
    if len(website) <= 0 or len(password) <= 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {mail}\n"
                                                              f"Password: {password}\nIs it ok to save?")
        if is_ok:
            with open("password.txt", "a") as file:
                file.write(f"{website} | {mail} | {password}\n")
                input_web.delete(0, len(website))
                input_password.delete(0, len(password))

# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = tkinter.Canvas(width=200, height=200)
image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)
website_label = tkinter.Label(text="Website:", font=("Arial", 9, "normal"))
website_label.grid(column=0, row=1)
input_web = tkinter.Entry(width=55)
input_web.grid(column=1, row=1, columnspan=2)
input_web.focus()
email = tkinter.Label(text="Email/Username:", font=("Arial", 9, "normal"))
email.grid(column=0, row=2)
input_mail = tkinter.Entry(width=55)
input_mail.grid(column=1, row=2, columnspan=2)
input_mail.insert(0, "bushra@gmail.com")
password_label = tkinter.Label(text="Password:", font=("Arial", 9, "normal"))
password_label.grid(column=0, row=3)
input_password = tkinter.Entry(width=35)
input_password.grid(column=1, row=3)
button_password = tkinter.Button(text="Generate Password", command=generate_password)
button_password.grid(column=2, row=3)
button_add = tkinter.Button(text="Add", width=45, command=save)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
