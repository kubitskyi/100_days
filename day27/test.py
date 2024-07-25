from tkinter import *


window = Tk()
window.title("My First Program")
window.minsize(width=500, height=300)

#lable
my_lable = Label(text="I Am a Label", font=('Arial', 24, 'bold'))
my_lable.grid(column=0,row=0)

my_lable["text"] = "New Text"
my_lable.config(text="New Text")

# Button
def button_click():
    new_text = input.get()
    my_lable.config(text=new_text)

button = Button(text="Click Me", command=button_click)
button.grid(column=1,row=1)

# Entry

input = Entry()
input.grid(column=2,row=2)



window.mainloop()