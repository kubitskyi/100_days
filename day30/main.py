from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [chr(i) for i in range(ord('a'), ord('z')+1)] + [chr(i) for i in range(ord('A'), ord('Z')+1)]
    numbers = [str(i) for i in range(0,9)]
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ':', ';','<', '>', ',', '.', '?', '/']
    
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password_entry.insert(0, "".join(password_list))
    


        
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entriy.get()
    email = email_entriy.get()
    password = password_entry.get()
    
    new_data = {
        website:{
            "email":email,
            "password":password
            }
        }
    
 
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message=("Please make sure you haven't left any fields empty."))
    else:  
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details \nEmail: {email} "
                            f"\nPassword: {password} \nIs it ok to save&?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entriy.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
              
                
def find_password():  
    website = website_entriy.get()           
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
         messagebox.showinfo(title="Error", message="No Data Fole Found.")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website.capitalize(), message=f"Email: {email}\nPasswor: {password}")
        else:
            messagebox.showinfo(title=website.capitalize(), message="Data not found")
           
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

#Lables
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label = Label(text="Password")
password_label.grid(row=3, column=0)

#Entries
website_entriy = Entry(width=20)
website_entriy.grid(row=1, column=1)
website_entriy.focus()
email_entriy = Entry(width=37)
email_entriy.grid(row=2, column=1, columnspan=2)
email_entriy.insert(0, "example@example.ua")
password_entry = Entry(width=20)
password_entry.grid(row=3, column=1)

#Buttons
search_button = Button(text="Search", width=12, command=find_password)
search_button.grid(row=1, column=2 )

generate_password_button = Button(text="Generate password", width=12, command=generate_password)
generate_password_button.grid(row=3,column=2)
add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
