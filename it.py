import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from tkinter import ttk

# Job profiles with importance weights for skills
job_profiles = {
    "Database Administrator": {
        "job": "Database Administrator",
        "skills": [8, 10, 9, 7, 5, 4, 2, 1, 3, 6],  # Weights for skills
        "courses": ["Database Management Systems", "SQL for Data Science", "Database Security"],
    },
    "Information Systems Manager": {
        "job": "Information Systems Manager",
        "skills": [6, 8, 7, 6, 5, 3, 9, 2, 1, 4],
        "courses": ["IT Governance", "Project Management Fundamentals", "Strategic Information Systems"],
    },
    "Business Intelligence Analyst": {
        "job": "Business Intelligence Analyst",
        "skills": [5, 6, 10, 8, 3, 4, 2, 1, 9, 7],
        "courses": ["Business Analytics with Excel", "Data Visualization with Tableau", "Data Warehousing Concepts"],
    },
    "Data Analyst": {
        "job": "Data Analyst",
        "skills": [4, 5, 8, 10, 3, 2, 7, 1, 9, 6],
        "courses": ["Data Analytics with Python", "Introduction to R for Data Science", "Data Visualization Best Practices"],
    },
    "Information Security Manager": {
        "job": "Information Security Manager",
        "skills": [7, 6, 5, 4, 10, 2, 8, 3, 9, 1],
        "courses": ["Risk Management in IT", "Cybersecurity Fundamentals", "Compliance and Regulatory Standards"],
    },
    "IT Support Specialist": {
        "job": "IT Support Specialist",
        "skills": [4, 3, 5, 6, 7, 10, 1, 2, 8, 9],
        "courses": ["CompTIA A+ Certification", "Networking Basics", "Operating System Fundamentals"],
    },
    "Enterprise Architect": {
        "job": "Enterprise Architect",
        "skills": [5, 4, 6, 8, 3, 7, 10, 9, 1, 2],
        "courses": ["Enterprise Architecture Frameworks", "Business Process Modeling", "IT Strategy Development"],
    },
    "Network Administrator": {
        "job": "Network Administrator",
        "skills": [6, 5, 4, 8, 7, 3, 2, 10, 1, 9],
        "courses": ["Networking Fundamentals", "Network Security", "Advanced Network Configuration"],
    },
    "Cloud Solutions Architect": {
        "job": "Cloud Solutions Architect",
        "skills": [8, 7, 5, 6, 4, 3, 9, 10, 2, 1],
        "courses": ["Cloud Computing Fundamentals", "AWS Certified Solutions Architect", "Azure Architecture"],
    },
    "Data Scientist": {
        "job": "Data Scientist",
        "skills": [9, 10, 7, 6, 5, 8, 4, 3, 2, 1],
        "courses": ["Machine Learning with Python", "Big Data Technologies", "Statistical Analysis"],
    },
}

# Dynamic fuzzy inference system implementation
def fuzzy_inference_system(skill_values):
    scores = {}
    for profile, data in job_profiles.items():
        score = sum(w * skill for w, skill in zip(data["skills"], skill_values))  # Weighted sum of skills
        scores[profile] = score

    # Get the profile with the highest score
    best_profile = max(scores, key=scores.get)
    return job_profiles[best_profile]

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
        for var in [database_var, systems_manager_var, business_intelligence_var,
                    data_analysis_var, security_manager_var, it_support_var,
                    enterprise_architect_var, network_admin_var, cloud_architect_var, data_scientist_var]:
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
    skills = ['Database Admin', 'Info Systems Manager', 'Business Intelligence', 'Data Analyst',
              'Info Security Manager', 'IT Support', 'Enterprise Architect', 'Network Admin',
              'Cloud Architect', 'Data Scientist']

    fig, ax = plt.subplots(figsize=(10, 6))

    colors = ['blue', 'green', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'brown', 'red', 'violet']
    
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

# GUIs
# Function to update the label with the current slider value
def update_label(slider_var, label):
    label.config(text=f"{int(slider_var.get())}")  # Update label with the current value

# Set up the main window
root = tk.Tk()
root.title("IT Career Pathway & Skill Enhancer")
root.geometry("600x900")  # Increased window size
root.configure(bg='#20B2B2')  # Light color background

# Skill ranking inputs
database_var = tk.DoubleVar()
systems_manager_var = tk.DoubleVar()
business_intelligence_var = tk.DoubleVar()
data_analysis_var = tk.DoubleVar()
security_manager_var = tk.DoubleVar()
it_support_var = tk.DoubleVar()
enterprise_architect_var = tk.DoubleVar()
network_admin_var = tk.DoubleVar()
cloud_architect_var = tk.DoubleVar()
data_scientist_var = tk.DoubleVar()

# Skill ranking labels and inputs
tk.Label(root, text="Rate your skills from 1 to 10", bg='#20B2B2', font=("Helvetica", 14)).pack(pady=10)

# Create a frame to hold the sliders
input_frame = tk.Frame(root, bg='#20B2B2')
input_frame.pack(pady=10)

skills = [
    "Database Administrator",
    "Information Systems Manager",
    "Business Intelligence Analyst",
    "Data Analyst",
    "Information Security Manager",
    "IT Support Specialist",
    "Enterprise Architect",
    "Network Administrator",
    "Cloud Solutions Architect",
    "Data Scientist"
]

skill_vars = [
    database_var,
    systems_manager_var,
    business_intelligence_var,
    data_analysis_var,
    security_manager_var,
    it_support_var,
    enterprise_architect_var,
    network_admin_var,
    cloud_architect_var,
    data_scientist_var
]

for i, skill in enumerate(skills):
    tk.Label(input_frame, text=f"{skill}:", bg='#20B2B2', font=("Helvetica", 12)).grid(row=i, column=0, padx=10, pady=5)

    slider_label = tk.Label(input_frame, text="5", bg='#20B2B2', font=("Helvetica", 12))  # Default value
    slider_label.grid(row=i, column=2, padx=10, pady=5)

    slider = ttk.Scale(input_frame, from_=1, to=10, variable=skill_vars[i], orient='horizontal',
                       command=lambda value, lbl=slider_label: lbl.config(text=int(float(value))))  # Update label on slider change
    slider.grid(row=i, column=1, padx=10, pady=5, sticky='ew')
    slider.set(5)  # Set initial value to 5 for all sliders

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_ranking, bg='lightgreen', font=("Helvetica", 12))
submit_button.pack(pady=20)

# Labels for displaying job and courses
job_label = tk.Label(root, text="", bg='#20B2B2', font=("Helvetica", 12))
job_label.pack(pady=10)

courses_label = tk.Label(root, text="", bg='#20B2B2', font=("Helvetica", 12))
courses_label.pack(pady=10)

suitability_label = tk.Label(root, text="", bg='#20B2B2', font=("Helvetica", 12))
suitability_label.pack(pady=10)

# Start the GUI loop
root.mainloop()
