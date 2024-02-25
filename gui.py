# Martin Meszaros
# The GUI for our application
# 25/02/2024
# V1.6

import tkinter as tk
from tkinter import ttk
import analyse


def submit_data():
    try:
        # Get integer values from entry widgets
        budget = int(entry1.get())
        years_plan = int(entry2.get())
        mileage_per_year = int(entry3.get())
        manufacturers = []
        if bool(check_var1.get()):
            manufacturers += ['audi']
        if bool(check_var2.get()):
            manufacturers += ['bmw']
        if bool(check_var3.get()):
            manufacturers += ['ford']
        if bool(check_var4.get()):
            manufacturers += ['hyundai']
        if bool(check_var5.get()):
            manufacturers += ['merc']
        if bool(check_var6.get()):
            manufacturers += ['skoda']
        if bool(check_var7.get()):
            manufacturers += ['toyota']
        if bool(check_var8.get()):
            manufacturers += ['vauxhall']
        if bool(check_var9.get()):
            manufacturers += ['vw']


        # Get cheapest, 2nd cheapest and 3rd cheapest options
        best,second_best,third_best = analyse.analyse_data(budget,years_plan,mileage_per_year,manufacturers)

        # Perform your query or action with the entered integers
        result_label.config(text=f"Options best fitting your criteria:\n----- ----- 1 ----- -----\n{best}")
        result_label2.config(text=f"\n----- ----- 2 ----- -----\n{second_best}")
        result_label3.config(text=f"\n----- ----- 3 ----- -----\n{third_best}")
    except ValueError:
        # Handle the case where the input is not an integer
        result_label.config(text="Please enter valid integers.")


def clear_entries():
    # Clear the entry widgets
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    result_label.config(text="")


def exit_app():
    root.destroy()


# Create the main window
root = tk.Tk()
root.title("Your Car Finder")

# Create a frame to hold the widgets
frame = ttk.Frame(root, padding="10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Add a welcome message label
welcome_label = ttk.Label(frame, text="Welcome to the Your Car Finder!\nI am going to help you find your next car.\nPlease state your requirements!")
welcome_label.grid(column=0, row=0, columnspan=2, pady=10)

# Create labels for the entry widgets
label1 = ttk.Label(frame, text="Budget(£):")
label2 = ttk.Label(frame, text="Planned ownership length(years):")
label3 = ttk.Label(frame, text="Annual mileage:")

# Create entry widgets
entry1 = ttk.Entry(frame)
entry2 = ttk.Entry(frame)
entry3 = ttk.Entry(frame)

# Create checkboxes for New Section 1
new_section1_label = ttk.Label(frame, text="Car manufacturers:")
check_var1 = tk.IntVar(value=1)
check_var2 = tk.IntVar(value=1)
check_var3 = tk.IntVar(value=1)
check_var4 = tk.IntVar(value=1)
check_var5 = tk.IntVar(value=1)
check_var6 = tk.IntVar(value=1)
check_var7 = tk.IntVar(value=1)
check_var8 = tk.IntVar(value=1)
check_var9 = tk.IntVar(value=1)
checkbox1 = ttk.Checkbutton(frame, text="Audi", variable=check_var1)
checkbox2 = ttk.Checkbutton(frame, text="BMW", variable=check_var2)
checkbox3 = ttk.Checkbutton(frame, text="Ford", variable=check_var3)
checkbox4 = ttk.Checkbutton(frame, text="Hyundai", variable=check_var4)
checkbox5 = ttk.Checkbutton(frame, text="Mercedes", variable=check_var5)
checkbox6 = ttk.Checkbutton(frame, text="Skoda", variable=check_var6)
checkbox7 = ttk.Checkbutton(frame, text="Toyota", variable=check_var7)
checkbox8 = ttk.Checkbutton(frame, text="Vauxhall", variable=check_var8)
checkbox9 = ttk.Checkbutton(frame, text="VW", variable=check_var9)

# Create checkboxes for New Section 2
new_section2_label = ttk.Label(frame, text="Fuel Type:")
check_var10 = tk.IntVar(value=1)
check_var11 = tk.IntVar(value=1)
check_var12 = tk.IntVar(value=1)
checkbox10 = ttk.Checkbutton(frame, text="Petrol", variable=check_var10)
checkbox11 = ttk.Checkbutton(frame, text="Diesel", variable=check_var11)
checkbox12 = ttk.Checkbutton(frame, text="Hybrid", variable=check_var12)


# Create a submit button
submit_button = ttk.Button(frame, text="Submit", command=submit_data)
clear_button = ttk.Button(frame, text="Clear", command=clear_entries)
exit_button = ttk.Button(frame, text="Exit", command=exit_app)

# Create a label to display the result
result_label = ttk.Label(frame, text="")
result_label2 = ttk.Label(frame, text="")
result_label3 = ttk.Label(frame, text="")


# Place the widgets in the grid
label1.grid(column=0, row=1, pady=5, sticky=tk.E)
label2.grid(column=0, row=2, pady=5, sticky=tk.E)
label3.grid(column=0, row=3, pady=5, sticky=tk.E)
entry1.grid(column=1, row=1, pady=5, sticky=tk.W)
entry2.grid(column=1, row=2, pady=5, sticky=tk.W)
entry3.grid(column=1, row=3, pady=5, sticky=tk.W)

# Place checkboxes for New Section 1
new_section1_label.grid(column=0, row=4, pady=5, sticky=tk.E)
checkbox1.grid(column=1, row=4, pady=5, sticky=tk.W)
checkbox2.grid(column=1, row=5, pady=5, sticky=tk.W)
checkbox3.grid(column=1, row=6, pady=5, sticky=tk.W)
checkbox4.grid(column=2, row=4, pady=5, sticky=tk.W)
checkbox5.grid(column=2, row=5, pady=5, sticky=tk.W)
checkbox6.grid(column=2, row=6, pady=5, sticky=tk.W)
checkbox7.grid(column=3, row=4, pady=5, sticky=tk.W)
checkbox8.grid(column=3, row=5, pady=5, sticky=tk.W)
checkbox9.grid(column=3, row=6, pady=5, sticky=tk.W)

# Place checkboxes for New Section 2
new_section2_label.grid(column=0, row=7, pady=5, sticky=tk.E)
checkbox10.grid(column=1, row=7, pady=5, sticky=tk.W)
checkbox11.grid(column=2, row=7, pady=5, sticky=tk.W)
checkbox12.grid(column=3, row=7, pady=5, sticky=tk.W)

# Place buttons
submit_button.grid(column=0, row=8, pady=5, sticky=tk.N)
clear_button.grid(column=1, row=8, pady=5, sticky=tk.N)
exit_button.grid(column=2, row=8, pady=5, sticky=tk.N)

# Place the result label
result_label.grid(column=0, row=9, pady=5, columnspan=3)
result_label2.grid(column=2, row=9, pady=5, columnspan=3)
result_label3.grid(column=12, row=9, pady=5, columnspan=3)


# Center the frame within the window
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Configure column weights to make the frame expandable
frame.columnconfigure(0, weight=1)
frame.columnconfigure(4, weight=1)

# Configure row weights to make the frame expandable
frame.rowconfigure(0, weight=1)
frame.rowconfigure(10, weight=1)

# Set the theme (optional)
# Available themes: "clam", "alt", "default", "classic"
ttk.Style().theme_use("clam")

# Start the Tkinter event loop
root.mainloop()

