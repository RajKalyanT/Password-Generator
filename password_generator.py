from tkinter import *
import random
import string

root = Tk()
root.geometry("400x280")
root.title("Password Generator")
root.configure(bg="#A6665E")

title = StringVar()
label = Label(root, textvariable=title, font=("Arial", 15, "bold"), bg="light blue", fg="blue")
label.pack()
title.set("The strength of password:")

choice = IntVar()
Radiobutton(root, text="POOR", variable=choice, value=1,fg="red",bg="#A6665E").pack(anchor=CENTER)
Radiobutton(root, text="MODERATE", variable=choice, value=2,fg="#B3D407",bg="#A6665E").pack(anchor=CENTER)
Radiobutton(root, text="GOOD", variable=choice, value=3,fg="green",bg="#A6665E").pack(anchor=CENTER)
label_choice = Label(root)
label_choice.pack()

len_label = StringVar()
len_label.set("Length of password:")
len_title = Label(root, textvariable=len_label, font=("Arial", 15, "bold"), bg="light blue", fg="blue")
len_title.pack()
val = IntVar()
Spinbox(root, from_=8, to=24, textvariable=val, width=13).pack()

def callback():
    password = passgen()
    lsum.config(text="Password: " + password,bg="#A6665E",fg="white")

passgen_button = Button(root, text="Generate Password", bd=5, height=2, command=callback)
passgen_button.pack()

lsum = Label(root)
lsum.pack(side=BOTTOM)

# Logic
poor_chars = string.ascii_uppercase + string.ascii_lowercase
moderate_chars = poor_chars + string.digits
symbols = "~`!@#$%^&*()_-+={[}]|\:;\"'<,>.?/"
good_chars = poor_chars + moderate_chars + symbols

def passgen():
    length = val.get()
    if choice.get() == 1:
        return "".join(random.sample(poor_chars, length))
    elif choice.get() == 2:
        return "".join(random.sample(moderate_chars, length))
    elif choice.get() == 3:
        return "".join(random.sample(good_chars, length))

root.mainloop()
