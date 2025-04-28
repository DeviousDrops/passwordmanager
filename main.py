from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pwdgen():
    rpass=''
    p_entry.delete(0,END)
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    combined=letters+numbers+symbols
    for i in range(15):
        rpass+=combined[random.randint(0, len(combined) - 1)]
    p_entry.insert(0,rpass)
    pyperclip.copy(rpass)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def delentry():
    w_entry.delete(0,END)
    p_entry.delete(0,END)


def save():

    website=w_entry.get()
    email=u_entry.get()
    password=p_entry.get()
    new_data={
        website: {
            "email":email,
            "password":password,
        }
    }

    if len(password)<8:
        messagebox.showwarning("Warning", "Password must be at least 8 characters long.")
        delentry()
    elif len(email)<5:
        messagebox.showwarning("Warning", "Username/email should be atleast 4 characters long.")
        delentry()
    elif website=='':
        messagebox.showwarning("Warning", "Enter the website name.")
        delentry()
    else:  
        try:
            with open("data.json","r") as dfile:
                data=json.load(dfile)
             
        except FileNotFoundError:
            with open("data.json","w") as dfile:
                json.dump(new_data,dfile,indent=4)
                delentry()
        else:
            data.update(new_data)    

            with open("data.json","w") as dfile:
                json.dump(data,dfile,indent=4)
                delentry()

        messagebox.showinfo("Success", "Details have been saved!")

# ----------------------------- SEARCH -------------------------------- #

def srch():
    website=w_entry.get()
    try:
        with open("data.json","r") as dfile:
                data=json.load(dfile)
    except FileNotFoundError:
        messagebox.showinfo("Failure", "The details were not found")
    else:
        if(website in data):
            em= data[website]["email"]
            pw=data[website]["password"]
            messagebox.showinfo("Success", f"Email/username:\t{em}\nPassword:\t{pw}")
        else:
            messagebox.showinfo("Failure", "The details were not found")


    

    


    

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)
canvas=Canvas(height=200,width=200)
lock=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock)
canvas.grid(column=1,row=0)
Web=Label(text="Website:")
user=Label(text="Email/Username:")
pwd=Label(text="Password:")
w_entry=Entry(width=21)
u_entry=Entry(width=35)
p_entry=Entry(width=21)
Web.grid(column=0,row=1, sticky="e")
user.grid(column=0,row=2, sticky="e")
pwd.grid(column=0,row=3, sticky="e")
w_entry.grid(column=1,row=1,padx=1, sticky="ew")
u_entry.grid(column=1,row=2,columnspan=2, sticky="ew")
p_entry.grid(column=1,row=3,padx=1, sticky="ew")
u_entry.insert(0,"ikartik.reddy@gmail.com")#change default email here
generate=Button(command=pwdgen,text="Generate Password",padx=1,pady=0.5,borderwidth=0.5,bg="white")
generate.grid(column=2,row=3)
search=Button(command=srch,text="Search",padx=1,borderwidth=0.5,pady=0.5,bg="white")
search.grid(column=2,row=1,sticky="ew")
Addpwd=Button(text="Add",width=36,borderwidth=0.5,bg="white",command=save)
Addpwd.grid(column=1,row=4,columnspan=2, sticky="ew")








window.mainloop()

