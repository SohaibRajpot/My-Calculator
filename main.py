import tkinter as tk
from tkinter import *
from tkinter import ttk
from kivy.app import App
from kivy.uix.button import*


def calculate_profit():

    try:
        buying_price = float(buying_price_entry.get())
        selling_price = float(selling_price_entry.get())
        amount = int(amount_entry.get())
        selected_currency = cb1.get()
        

        if selling_price > buying_price:
            quantity_in_dollar = amount / buying_price
            profit_in_selected_currency = amount / buying_price * (selling_price - buying_price)
            percentage = profit_in_selected_currency * 100 / amount

            quantity_label.config(text=f"Quantity in dollar: {quantity_in_dollar:.2f}",font="Arial 12 bold")
            profit_label.config(text=f"Profit in {selected_currency}: {profit_in_selected_currency:.2f}",font="Arial 12 bold")
            percentage_label.config(text=f"Percentage: {percentage:.2f}%",font="Arial 12 bold")
        else:
            quantity_label.config(text="Selling price must be greater than buying price",font="Arial 12 bold")
    except ValueError:
        quantity_label.config(text="Please enter valid numeric values",font="Arial 12 bold")

# Create the main window
root = tk.Tk()
root.title("P Calculator")
root.iconbitmap("calculator.ico")
root.minsize(600,600)

# Welcome Message
f1=Frame(root,borderwidth=9,relief=SUNKEN,)
f1.pack(side=TOP,fill="x")
welcome_label = tk.Label(f1, text="Welcome to P Calculator", font=("Helvetica", 35, "bold"))
welcome_label.pack(side=TOP,padx=20,pady=20)

# Labels and Entry Widgets
buying_price_label = tk.Label(root, text="Enter the buying price",font="Helvetica 16 bold")
buying_price_label.pack(pady=5)
buying_price_entry = tk.Entry(root,width=30,font="Arial 12 bold",borderwidth=6,relief=SUNKEN)
buying_price_entry.pack(padx=5,pady=5)

selling_price_label = tk.Label(root, text="Enter the selling price ",font="Helvetica 16 bold")
selling_price_label.pack(pady=5)
selling_price_entry = tk.Entry(root,width=30,font="Arial 12 bold",borderwidth=6,relief=SUNKEN)
selling_price_entry.pack(padx=5,pady=5)

amount_label = tk.Label(root, text="Enter the Investment",font="Helvetica 16 bold")
amount_label.pack(pady=5)
amount_entry = tk.Entry(root,width=30,font="Arial 12 bold",borderwidth=6,relief=SUNKEN)
amount_entry.pack(padx=5,pady=5)

quantity_label = tk.Label(root, text="")
quantity_label.pack()
profit_label = tk.Label(root, text="")
profit_label.pack()
percentage_label = tk.Label(root, text="")
percentage_label.pack()

calculate_button = tk.Button(root,fg="white",bg="black",font="Arial 20 bold" ,borderwidth=6,relief=SUNKEN,text="Calculate", command=calculate_profit)
calculate_button.pack()




# Combo box for currency selection
selected_currency = ["PKR", "GBP", "AED", "USD", "EURO"]
cb1 = ttk.Combobox(root, values=selected_currency, width=6,height=3,state="readonly")
cb1.set("PKR")
cb1.pack(padx=5, pady=5)







# Run the Tkinter main loop
root.mainloop()
