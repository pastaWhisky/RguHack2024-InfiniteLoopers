import tkinter as tk
from tkinter import messagebox

def show_output():
    selected_car_types = [car_type.get() for car_type, var in car_type_vars.items() if var.get()]
    selected_fuel_types = [fuel_type.get() for fuel_type, var in fuel_type_vars.items() if var.get()]
    selected_transmission_types = [transmission_type.get() for transmission_type, var in transmission_type_vars.items() if var.get()]

    # Print output in the GUI
    output_message = f"Your answers:\n\
        Car Types: {', '.join(selected_car_types)}\n\
        Fuel Types: {', '.join(selected_fuel_types)}\n\
        Transmission Types: {', '.join(selected_transmission_types)}"
    messagebox.showinfo("Output", output_message)

# Create the main window
root = tk.Tk()
root.title("Car Selection GUI")
# Add three labels to ask questions
question_label1 = tk.Label(root, text="What is your budget for a car")
question_label1.pack(pady=5)

# Entry widget for the first question
entry1 = tk.Entry(root, width=30)
entry1.pack(pady=5)

question_label2 = tk.Label(root, text=" How many years would the car be used")
question_label2.pack(pady=5)

# Entry widget for the second question
entry2 = tk.Entry(root, width=30)
entry2.pack(pady=5)

question_label3 = tk.Label(root, text="How much miles would you drive per year")
question_label3.pack(pady=5)

# Entry widget for the second question
entry3 = tk.Entry(root, width=30)
entry3.pack(pady=5)

# Set a background color
root.configure(bg="#0000FF")

# Add labels and checkboxes for car selection
label_style = {"font": ("Arial", 12), "bg": "#FFC0CB", "pady": 5}

car_type_label = tk.Label(root, text="Select Car Types:", **label_style)
car_type_label.pack()

car_types = ["Audi", "BMW", "Skoda", "Mercedes", "Ford", "Hyundai", "Toyota", "Vauxhall", "VW"]
car_type_vars = {car_type: tk.BooleanVar() for car_type in car_types}

for car_type in car_types:
    checkbox = tk.Checkbutton(root, text=car_type, variable=car_type_vars[car_type], onvalue=True, offvalue=False)
    checkbox.pack()

fuel_type_label = tk.Label(root, text="Select Fuel Types:", **label_style)
fuel_type_label.pack()

fuel_types = ["Petrol", "Diesel", "Hybrid"]
fuel_type_vars = {fuel_type: tk.BooleanVar() for fuel_type in fuel_types}

for fuel_type in fuel_types:
    checkbox = tk.Checkbutton(root, text=fuel_type, variable=fuel_type_vars[fuel_type], onvalue=True, offvalue=False)
    checkbox.pack()

transmission_type_label = tk.Label(root, text="Select Transmission Types:", **label_style)
transmission_type_label.pack()

transmission_types = ["Manual", "Automatic", "Semi-Auto"]
transmission_type_vars = {transmission_type: tk.BooleanVar() for transmission_type in transmission_types}

for transmission_type in transmission_types:
    checkbox = tk.Checkbutton(root, text=transmission_type, variable=transmission_type_vars[transmission_type], onvalue=True, offvalue=False)
    checkbox.pack()

# Add a button with custom style to submit the answers
button_style = {"font": ("Arial", 14), "bg": "#4CAF50", "fg": "pink", "padx": 10, "pady": 5}
submit_button = tk.Button(root, text="Submit", command=show_output, **button_style)
submit_button.pack(pady=10)

# Run the main event loop
root.mainloop()
