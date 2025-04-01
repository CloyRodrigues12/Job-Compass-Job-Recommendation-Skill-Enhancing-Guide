import tkinter as tk
from tkinter import ttk
import subprocess  # To open different files

# Function to handle category selection and open respective file
def proceed():
    selected_category = category_var.get()
    category_files = {
        "Engineering": "engineering.py",
        "Medical": "medical.py",
        "Business and Finance": "business&finance.py",
        "Information Technology": "it.py",
        "Arts & Design": "arts.py"
    }
    
    # Get the corresponding file for the selected category
    file_to_open = category_files.get(selected_category)
    if file_to_open:
        # Run the respective file for the selected category
        subprocess.run(["python", file_to_open])

# Function to create a gradient background
def create_gradient(canvas, width, height, color1, color2):
    for i in range(height):
        # Calculate the color for each line
        r = int(color1[0] + (color2[0] - color1[0]) * (i / height))
        g = int(color1[1] + (color2[1] - color1[1]) * (i / height))
        b = int(color1[2] + (color2[2] - color1[2]) * (i / height))
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_line(0, i, width, i, fill=color)

# Set up the main window
root = tk.Tk()
root.title("Job Recommendation & Skill Enhancing Guide") 
root.geometry("700x500")

# Calculate position x and y to center the window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 700
window_height = 500
position_x = (screen_width - window_width) // 2
position_y = (screen_height - window_height) // 2

# Set the geometry with the calculated position
root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

# Create a canvas for the gradient background
canvas = tk.Canvas(root, width=600, height=400)
canvas.pack(fill="both", expand=True)

# Define gradient colors (RGB)
color1 = (230, 255, 230)  # Light green
color2 = (102, 179, 255)  # Light blue

# Create the gradient background
create_gradient(canvas, 1530, 750, color1, color2)

# Frame to hold the other widgets
frame = tk.Frame(canvas, bg='white', bd=20)
frame.place(relx=0.5, rely=0.5, anchor='center')

title_label = tk.Label(frame, text="Welcome to Job Recommendation ", font=("Helvetica", 18, "bold"), bg='white')
title_label.pack(pady=10)
title_label = tk.Label(frame, text="& Skill Enhancing Guide", font=("Helvetica", 18, "bold"), bg='white')
title_label.pack(pady=1)


category_label = tk.Label(frame, text="Please select your career category:", font=("Helvetica", 12), bg='white')
category_label.pack(pady=20)

# Dropdown for category selection
category_var = tk.StringVar()
career_categories = ["Engineering", "Medical", "Business and Finance", "Information Technology", "Arts & Design"]
category_dropdown = ttk.Combobox(frame, textvariable=category_var, values=career_categories, state="readonly", font=("Helvetica", 15))
category_dropdown.pack(pady=15)

proceed_button = tk.Button(frame, text="Proceed", command=proceed, font=("Helvetica", 12), bg='#66b3ff', fg="white", padx=10, pady=5)
proceed_button.pack(pady=20)

root.mainloop()