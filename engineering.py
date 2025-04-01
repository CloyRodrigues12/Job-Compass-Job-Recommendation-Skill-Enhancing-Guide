# engineering.py
import tkinter as tk
import subprocess  # To open different files
import sys

# Function to handle field selection and open the respective file
def open_field_file(field):
    field_files = {
        "Electronics and Computer Science": "electronics.py",
        "Computer Engineering": "computer_eng.py",
        "Mechanical Engineering": "mechanical_eng.py",
        "Civil Engineering": "civil_eng.py"
    }
    
    # Get the corresponding file for the selected field
    file_to_open = field_files.get(field)
    if file_to_open:
        # Run the respective file for the selected field
        subprocess.run([sys.executable, file_to_open])

# Set up the main window
root = tk.Tk()
root.title("Engineering Career Paths")
root.geometry("500x400")

# Calculate position x and y to center the window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 700
window_height = 500
position_x = (screen_width - window_width) // 2
position_y = (screen_height - window_height) // 2

# Set the geometry with the calculated position
root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

# Title label
title_label = tk.Label(root, text="Explore Your Engineering Career Path", font=("Helvetica", 16, "bold"))
title_label.pack(pady=20)

# Instruction label
instruction_label = tk.Label(root, text="Please select your field of interest:", font=("Helvetica", 12))
instruction_label.pack(pady=10)

# Buttons for each engineering field
fields = [
    "Electronics and Computer Science",
    "Computer Engineering",
    "Mechanical Engineering",
    "Civil Engineering"
]

for field in fields:
    # Creating buttons for each field
    field_button = tk.Button(root, text=field, font=("Helvetica", 12), width=30, 
    command=lambda f=field: open_field_file(f), bg="#4CAF50", fg="white")
    field_button.pack(pady=5)

# Start the GUI loop
root.mainloop()
