from tkinter import *


window = Tk()
window.title("Calculator")
window.config(padx=20, pady=20)

def calculate():
    miles = int(input_miles.get())
    km = round(miles * 1.609344)
    kilometers_lable.config(text=f"{km} km")

input_miles = Entry()
input_miles.grid(column=2,row=1)

miles_lable = Label(text="miles")
miles_lable.grid(column=3,row=1)

is_equal_lable = Label(text="is equal")
is_equal_lable.grid(column=1,row=2)

kilometers_lable = Label(text="0 km")
kilometers_lable.grid(column=2,row=2)

calculate_button = Button(text="calculate", command=calculate)
calculate_button.grid(column=2,row=3)


window.mainloop()