import tkinter as tk
from tkinter import ttk
import analyse

def submit_data():
    try:
        # Get integer values from entry widgets
        budget = int(entry1.get())
        years_plan = int(entry2.get())
        mileage_per_year = int(entry3.get())

        # Perform your query or action with the entered integers
        result_label.config(text=f"The best car fitting your criteria is:\n{analyse.analyse_data(budget,years_plan,mileage_per_year)}")

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
label2 = ttk.Label(frame, text="Planned ownership length:")
label3 = ttk.Label(frame, text="Annual mileage:")

# Create entry widgets
entry1 = ttk.Entry(frame)
entry2 = ttk.Entry(frame)
entry3 = ttk.Entry(frame)

# Create a submit button
submit_button = ttk.Button(frame, text="Submit", command=submit_data)
clear_button = ttk.Button(frame, text="Clear", command=clear_entries)
exit_button = ttk.Button(frame, text="Exit", command=exit_app)

# Create a label to display the result
result_label = ttk.Label(frame, text="")

# Place the widgets in the grid
label1.grid(column=0, row=1, pady=5, sticky=tk.E)
label2.grid(column=0, row=2, pady=5, sticky=tk.E)
label3.grid(column=0, row=3, pady=5, sticky=tk.E)
entry1.grid(column=1, row=1, pady=5, sticky=tk.W)
entry2.grid(column=1, row=2, pady=5, sticky=tk.W)
entry3.grid(column=1, row=3, pady=5, sticky=tk.W)
submit_button.grid(column=1, row=4, pady=10, sticky=tk.N)
clear_button.grid(column=2, row=4, pady=5, sticky=tk.N)
exit_button.grid(column=0, row=4, pady=5, sticky=tk.N)
result_label.grid(column=1, row=5, pady=5)

# Configure column weights to make the frame expandable
frame.columnconfigure(0, weight=1)
frame.columnconfigure(2, weight=1)

# Configure row weights to make the frame expandable
frame.rowconfigure(0, weight=1)
frame.rowconfigure(6, weight=1)

# Set the theme (optional)
# Available themes: "clam", "alt", "default", "classic"
ttk.Style().theme_use("clam")

# Start the Tkinter event loop
root.mainloop()

