import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from tkinter import ttk

# Business & Finance job profiles and associated courses
job_profiles = {
    "Financial Analyst": {
        "job": "Financial Analyst",
        "courses": ["Financial Modeling", "Corporate Finance", "Investment Analysis"],
    },
    "Marketing Specialist": {
        "job": "Marketing Specialist",
        "courses": ["Digital Marketing", "Market Research", "Consumer Behavior"],
    },
    "Project Manager": {
        "job": "Project Manager",
        "courses": ["Project Management Basics", "Agile Methodologies", "Leadership Skills"],
    },
    "Investment Banker": {
        "job": "Investment Banker",
        "courses": ["Investment Banking Fundamentals", "Mergers & Acquisitions", "Financial Markets"],
    },
    "Business Consultant": {
        "job": "Business Consultant",
        "courses": ["Strategic Management", "Consulting Fundamentals", "Business Development"],
    },
    "Sales Manager": {
        "job": "Sales Manager",
        "courses": ["Sales Strategy", "Negotiation Skills", "Customer Relationship Management"],
    },
    "Data Analyst": {
        "job": "Data Analyst",
        "courses": ["Data Analysis for Business", "Excel for Business", "Power BI"],
    },
    "Risk Manager": {
        "job": "Risk Manager",
        "courses": ["Risk Management Essentials", "Enterprise Risk Management", "Credit Risk Analysis"],
    },
    "Economist": {
        "job": "Economist",
        "courses": ["Microeconomics", "Macroeconomics", "Economic Forecasting"],
    },
    "Operations Manager": {
        "job": "Operations Manager",
        "courses": ["Operations Management", "Supply Chain Management", "Lean Processes"],
    },
}

# Fuzzy Inference System Implementation
def fuzzy_inference_system(skill_values):
    if skill_values[0] > 8:  # Strong in Financial Analysis
        return job_profiles["Financial Analyst"]
    elif skill_values[1] > 8:  # Strong in Marketing Strategy
        return job_profiles["Marketing Specialist"]
    elif skill_values[2] > 7:  # Strong in Business Communication
        return job_profiles["Business Consultant"]
    elif skill_values[3] > 7:  # Strong in Project Management
        return job_profiles["Project Manager"]
    elif skill_values[4] > 7:  # Strong in Data Analysis
        return job_profiles["Data Analyst"]
    elif skill_values[5] > 7:  # Strong in Investment Management
        return job_profiles["Investment Banker"]
    elif skill_values[6] > 7:  # Strong in Economic Knowledge
        return job_profiles["Economist"]
    elif skill_values[7] > 7:  # Strong in Leadership
        return job_profiles["Operations Manager"]
    elif skill_values[8] > 7:  # Strong in Sales Strategy
        return job_profiles["Sales Manager"]
    elif skill_values[9] > 7:  # Strong in Risk Management
        return job_profiles["Risk Manager"]
    else:
        return job_profiles["Business Consultant"]

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
        for var in skill_vars:
            validated_value = validate_input(var.get())
            if validated_value is None:
                raise ValueError("Please enter rankings between 1 and 10.")
            skill_values.append(validated_value)

        # Use fuzzy inference to get job recommendation
        profile = fuzzy_inference_system(skill_values)

        # Calculate suitability percentage
        total_rank = sum(skill_values)
        suitability = (max(skill_values) / total_rank) * 100 if total_rank else 0

        # Display job and courses
        job_label.config(text=f"Recommended Job: {profile['job']}")
        courses_label.config(text="Suggested Courses: " + ", ".join(profile["courses"]))
        suitability_label.config(text=f"Suitability Percentage: {suitability:.2f}%")

        # Plotting the membership graph
        plot_membership(skill_values, profile['job'])

    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))

# Function to plot the membership graph
def plot_membership(skill_values, job_title):
    x = np.arange(0, 11, 1)
    skills = ['Financial Analysis', 'Marketing Strategy', 'Business Communication',
              'Project Management', 'Data Analysis', 'Investment Management',
              'Economic Knowledge', 'Leadership', 'Sales Strategy', 'Risk Management']
    
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = ['#ff6961', '#77dd77', '#fdfd96', '#84b6f4', '#fdcae1', '#c23b22', '#f49ac2', '#aec6cf', '#ffb347', '#b19cd9']
    
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

# GUI
# Function to update the label with the current slider value
def update_label(slider_var, label):
    label.config(text=f"{int(slider_var.get())}")  # Update label with the current value

# Set up the main window
root = tk.Tk()
root.title("Business & Finance Career Guide")
root.geometry("600x900")
root.configure(bg='#7B7C7D')  # Light pink background

# Skill ranking inputs
skill_vars = [tk.DoubleVar() for _ in range(10)]

# Skill ranking labels and inputs
tk.Label(root, text="Rate your skills from 1 to 10", bg='#7B7C7D', font=("Helvetica", 14)).pack(pady=10)

# Create a frame to hold the sliders
input_frame = tk.Frame(root, bg='#7B7C7D')
input_frame.pack(pady=10)

skills = [
    "Financial Analysis", "Marketing Strategy", "Business Communication",
    "Project Management", "Data Analysis", "Investment Management",
    "Economic Knowledge", "Leadership", "Sales Strategy", "Risk Management"
]

for i, skill in enumerate(skills):
    tk.Label(input_frame, text=f"{skill}:", bg='#7B7C7D', font=("Helvetica", 12)).grid(row=i, column=0, padx=10, pady=5)
    
    slider_label = tk.Label(input_frame, text="5", bg='#7B7C7D', font=("Helvetica", 12))
    slider_label.grid(row=i, column=2, padx=10, pady=5)
    
    slider = ttk.Scale(input_frame, from_=1, to=10, variable=skill_vars[i], orient='horizontal',
                       command=lambda value, lbl=slider_label: lbl.config(text=int(float(value))))
    slider.grid(row=i, column=1, padx=10, pady=5, sticky='ew')
    slider.set(5)  # Set initial value to 5 for all sliders

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_ranking, bg='#36454F', font=("Helvetica", 12))
submit_button.pack(pady=20)

# Labels for displaying job and courses
job_label = tk.Label(root, text="", bg='#7B7C7D', font=("Helvetica", 12))
job_label.pack(pady=10)

courses_label = tk.Label(root, text="", bg='#7B7C7D', font=("Helvetica", 12))
courses_label.pack(pady=10)

suitability_label = tk.Label(root, text="", bg='#7B7C7D', font=("Helvetica", 12))
suitability_label.pack(pady=10)

# Start the GUI loop
root.mainloop()
