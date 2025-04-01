import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz

# Expanded job profiles with associated courses
job_profiles = {
    "Electronics Engineer": {
        "courses": ["Circuit Design Basics", "Embedded Systems", "Digital Signal Processing"],
    },
    "Software Developer": {
        "courses": ["Data Structures and Algorithms", "Web Development", "Machine Learning"],
    },
    "Systems Engineer": {
        "courses": ["IoT Development", "Full Stack Development", "Networking Essentials"],
    },
    "Data Scientist": {
        "courses": ["Statistics for Data Science", "Data Mining", "Machine Learning"],
    },
    "Network Engineer": {
        "courses": ["Networking Essentials", "Network Security", "Cloud Computing"],
    },
    "Embedded Systems Engineer": {
        "courses": ["Microcontroller Programming", "Real-Time Operating Systems", "IoT Fundamentals"],
    },
    "Firmware Engineer": {
        "courses": ["Embedded C Programming", "Digital Circuit Design", "Firmware Development"],
    },
    "DevOps Engineer": {
        "courses": ["Continuous Integration/Continuous Deployment", "Containerization", "Cloud Services"],
    },
    "AI Engineer": {
        "courses": ["Artificial Intelligence Fundamentals", "Deep Learning", "Natural Language Processing"],
    },
    "Cybersecurity Analyst": {
        "courses": ["Ethical Hacking", "Network Security", "Cybersecurity Fundamentals"],
    },
    "Database Administrator": {
        "courses": ["SQL and Database Management", "Data Warehousing", "Big Data Technologies"],
    },
    "Mobile App Developer": {
        "courses": ["Android Development", "iOS Development", "Cross-Platform Development"],
    },
    "Game Developer": {
        "courses": ["Game Design Principles", "Unity Game Development", "Graphics Programming"],
    },
    "Robotics Engineer": {
        "courses": ["Robotics Fundamentals", "Robot Operating System (ROS)", "Mechatronics"],
    },
    "Hardware Engineer": {
        "courses": ["PCB Design", "Hardware Testing", "FPGA Development"],
    },
    # Add more profiles as needed
}

# Fuzzy Inference System Implementation
def fuzzy_inference_system(skill_values):
    # Define thresholds for different job profiles
    if skill_values[0] > 7 and skill_values[3] > 6:  # Circuit Design & Embedded Systems
        return "Electronics Engineer", job_profiles["Electronics Engineer"]
    elif skill_values[1] > 7 and skill_values[2] > 6:  # Programming & Data Structures
        return "Software Developer", job_profiles["Software Developer"]
    elif skill_values[2] > 7 and skill_values[9] > 6:  # Data Structures & Networking
        return "Network Engineer", job_profiles["Network Engineer"]
    elif skill_values[1] > 7 and skill_values[8] > 6:  # Programming & Machine Learning
        return "Data Scientist", job_profiles["Data Scientist"]
    elif skill_values[0] > 6 and skill_values[6] > 6:  # Circuit Design & Microcontrollers
        return "Embedded Systems Engineer", job_profiles["Embedded Systems Engineer"]
    elif skill_values[1] > 6 and skill_values[8] > 6:  # Programming & Machine Learning
        return "AI Engineer", job_profiles["AI Engineer"]
    elif skill_values[5] > 7 and skill_values[2] > 6:  # Signal Processing & Data Structures
        return "Cybersecurity Analyst", job_profiles["Cybersecurity Analyst"]
    elif skill_values[1] > 6 and skill_values[3] > 6:  # Programming & DevOps
        return "DevOps Engineer", job_profiles["DevOps Engineer"]
    elif skill_values[4] > 7:  # Digital Logic Design
        return "Robotics Engineer", job_profiles["Robotics Engineer"]
    else:
        return "Systems Engineer", job_profiles["Systems Engineer"]  # Default case if no specific profile matches

# Function to validate input
def validate_input(input_value):
    try:
        value = int(input_value)
        if 1 <= value <= 10:
            return value
        else:
            raise ValueError
    except ValueError:
        return None

# Function to handle skill ranking and show recommendations
def submit_ranking():
    try:
        skill_values = []
        for var in [circuit_design_var, programming_var, data_structures_var,
                    embedded_systems_var, digital_logic_var, signal_processing_var,
                    microcontrollers_var, software_engineering_var,
                    machine_learning_var, networking_var]:
            validated_value = validate_input(var.get())
            if validated_value is None:
                raise ValueError("Please enter rankings between 1 and 10.")
            skill_values.append(validated_value)

        job_title, profile = fuzzy_inference_system(skill_values)  # Get job title and profile
        total_rank = sum(skill_values)
        suitability = (max(skill_values) / total_rank) * 100 if total_rank else 0

        job_label.config(text=f"Recommended Job: {job_title}")
        courses_label.config(text="Suggested Courses: " + ", ".join(profile["courses"]))
        suitability_label.config(text=f"Suitability Percentage: {suitability:.2f}%")
        plot_membership(skill_values, job_title)

    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))

# Function to plot the membership graph
def plot_membership(skill_values, job_title):
    x = np.arange(0, 11, 1)
    skills = ['Circuit Design', 'Programming', 'Data Structures', 'Embedded Systems',
              'Digital Logic', 'Signal Processing', 'Microcontrollers', 'Software Engineering',
              'Machine Learning', 'Networking']
    
    fig, ax = plt.subplots(figsize=(10, 6))

    colors = ['blue', 'green', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'lightblue', 'lime', 'salmon']
    
    # Plot fuzzy membership curves for each skill with shading
    for i, (skill, value) in enumerate(zip(skills, skill_values)):
        membership = fuzz.gaussmf(x, value, 1.5)
        ax.plot(x, membership, color=colors[i], label=f'{skill} ({value})')
        ax.fill_between(x, 0, membership, color=colors[i], alpha=0.3)

    ax.set_title(f'Membership Contributions for {job_title}')
    ax.set_xlabel('Skill Level')
    ax.set_ylabel('Degree of Membership')
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
    plt.tight_layout()
    plt.show()

# GUI Setup
def update_label(slider_var, label):
    label.config(text=f"{int(slider_var.get())}")  # Update label with the current value

# Set up the main window
root = tk.Tk()
root.title("Electronics and Computer Science Career Guide")
root.geometry("600x900")  # Adjusted window size
root.configure(bg='#ff8a65')  # Unique aesthetic shade (light blue)

# Skill ranking inputs
circuit_design_var = tk.DoubleVar()
programming_var = tk.DoubleVar()
data_structures_var = tk.DoubleVar()
embedded_systems_var = tk.DoubleVar()
digital_logic_var = tk.DoubleVar()
signal_processing_var = tk.DoubleVar()
microcontrollers_var = tk.DoubleVar()
software_engineering_var = tk.DoubleVar()
machine_learning_var = tk.DoubleVar()
networking_var = tk.DoubleVar()

tk.Label(root, text="Rate your skills from 1(Lowest) to 10(Highest)", bg='#ff8a65', font=("Helvetica", 14)).pack(pady=10)

# Create a frame to hold the sliders
input_frame = tk.Frame(root, bg='#ff8a65')
input_frame.pack(pady=10)

skills = [
    "Circuit Design",
    "Programming",
    "Data Structures",
    "Embedded Systems",
    "Digital Logic Design",
    "Signal Processing",
    "Microcontrollers",
    "Software Engineering",
    "Machine Learning",
    "Networking"
]

skill_vars = [
    circuit_design_var,
    programming_var,
    data_structures_var,
    embedded_systems_var,
    digital_logic_var,
    signal_processing_var,
    microcontrollers_var,
    software_engineering_var,
    machine_learning_var,
    networking_var
]

for i, skill in enumerate(skills):
    tk.Label(input_frame, text=f"{skill}:", bg='#ff8a65', font=("Helvetica", 12)).grid(row=i, column=0, padx=10, pady=5)
    
    slider_label = tk.Label(input_frame, text="5", bg='#ff8a65', font=("Helvetica", 12))  # Default value
    slider_label.grid(row=i, column=2, padx=10, pady=5)
    
    slider = ttk.Scale(input_frame, from_=1, to=10, variable=skill_vars[i], orient='horizontal',
    command=lambda value, lbl=slider_label: lbl.config(text=int(float(value))))  # Update label on slider change
    slider.grid(row=i, column=1, padx=10, pady=5, sticky='ew')
    slider.set(5)  # Set initial value to 5 for all sliders

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_ranking, bg='#ff5722', font=("Helvetica", 12))
submit_button.pack(pady=20)

# Labels for displaying job and courses
job_label = tk.Label(root, text="", bg='#ff8a65', font=("Helvetica", 12))
job_label.pack(pady=10)

courses_label = tk.Label(root, text="", bg='#ff8a65', font=("Helvetica", 12))
courses_label.pack(pady=10)

suitability_label = tk.Label(root, text="", bg='#ff8a65', font=("Helvetica", 12))
suitability_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
