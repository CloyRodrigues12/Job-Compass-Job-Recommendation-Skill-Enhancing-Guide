import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from tkinter import ttk

# Expanded job profiles with associated courses for Computer Science Engineering
job_profiles = {
    "Software Developer": {
        "job": "Software Developer",
        "courses": ["Data Structures and Algorithms", "Web Development", "Machine Learning"],
    },
    "Data Scientist": {
        "job": "Data Scientist",
        "courses": ["Data Analysis with Python", "Machine Learning Specialization", "Big Data Technologies"],
    },
    "AI Engineer": {
        "job": "AI Engineer",
        "courses": ["Artificial Intelligence Foundations", "Deep Learning", "Natural Language Processing"],
    },
    "Cloud Solutions Architect": {
        "job": "Cloud Solutions Architect",
        "courses": ["Cloud Computing Basics", "AWS Solutions Architect", "Azure Fundamentals"],
    },
    "Software Tester": {
        "job": "Software Tester",
        "courses": ["Software Testing Fundamentals", "Automation Testing", "Agile Testing Techniques"],
    },
    "Network Engineer": {
        "job": "Network Engineer",
        "courses": ["Network Fundamentals", "CCNA Certification", "Wireless Networking"],
    },
    "DevOps Engineer": {
        "job": "DevOps Engineer",
        "courses": ["DevOps Fundamentals", "Continuous Integration/Continuous Deployment", "Cloud Infrastructure Management"],
    },
    "Systems Analyst": {
        "job": "Systems Analyst",
        "courses": ["Systems Analysis and Design", "Business Analysis", "Enterprise Architecture"],
    },
    "Web Developer": {
        "job": "Web Developer",
        "courses": ["HTML, CSS, JavaScript", "Frontend Frameworks", "Backend Development"],
    },
    "Database Administrator": {
        "job": "Database Administrator",
        "courses": ["Database Management Systems", "SQL Fundamentals", "Data Warehousing"],
    },
    "Mixed": {
        "job": "Mixed Engineer",
        "courses": ["General Software Engineering", "Cross-Disciplinary Studies"],
    },
}

# Fuzzy Inference System Implementation
def fuzzy_inference_system(skill_values):
    if skill_values[0] > 8:  # High ranking in Programming
        return job_profiles["Software Developer"]
    elif skill_values[1] > 8:  # High ranking in Machine Learning
        return job_profiles["Data Scientist"]
    elif skill_values[2] > 7:  # Strong in AI concepts
        return job_profiles["AI Engineer"]
    elif skill_values[3] > 7:  # Strong in Cloud technologies
        return job_profiles["Cloud Solutions Architect"]
    elif skill_values[4] > 7:  # Strong in Testing
        return job_profiles["Software Tester"]
    elif skill_values[5] > 7:  # Strong in Networking
        return job_profiles["Network Engineer"]
    elif skill_values[6] > 7:  # Strong in Web Development
        return job_profiles["Web Developer"]
    elif skill_values[7] > 7:  # Strong in Databases
        return job_profiles["Database Administrator"]
    elif skill_values[8] > 7:  # Strong in Software Design
        return job_profiles["DevOps Engineer"]
    elif skill_values[9] > 7:  # Strong in Version Control
        return job_profiles["Systems Analyst"]
    else:
        return job_profiles["Mixed"]

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
        for var in [programming_var, machine_learning_var, ai_concepts_var, 
                    cloud_technologies_var, testing_var, networking_var, 
                    web_development_var, databases_var, 
                    software_design_var, version_control_var]:
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
    skills = ['Programming', 'Machine Learning', 'AI Concepts', 'Cloud Technologies',
              'Testing', 'Networking', 'Web Development', 'Databases',
              'Software Design', 'Version Control']
    
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


#GUIS
# Function to update the label with the current slider value
def update_label(slider_var, label):
    label.config(text=f"{int(slider_var.get())}")  # Update label with the current value

# Set up the main window
root = tk.Tk()
root.title("Computer Science Engineering Career Guide")
root.geometry("600x900")  # Increased window size
root.configure(bg='lightblue')  # Light color background

# Skill ranking inputs
programming_var = tk.DoubleVar()
machine_learning_var = tk.DoubleVar()
ai_concepts_var = tk.DoubleVar()
cloud_technologies_var = tk.DoubleVar()
testing_var = tk.DoubleVar()
networking_var = tk.DoubleVar()
web_development_var = tk.DoubleVar()
databases_var = tk.DoubleVar()
software_design_var = tk.DoubleVar()
version_control_var = tk.DoubleVar()

# Skill ranking labels and inputs
tk.Label(root, text="Rate your skills from 1 to 10", bg='lightblue', font=("Helvetica", 14)).pack(pady=10)

# Create a frame to hold the sliders
input_frame = tk.Frame(root, bg='lightblue')
input_frame.pack(pady=10)

skills = [
    "Programming",
    "Machine Learning",
    "AI Concepts",
    "Cloud Technologies",
    "Testing",
    "Networking",
    "Web Development",
    "Databases",
    "Software Design",
    "Version Control"
]

skill_vars = [
    programming_var,
    machine_learning_var,
    ai_concepts_var,
    cloud_technologies_var,
    testing_var,
    networking_var,
    web_development_var,
    databases_var,
    software_design_var,
    version_control_var
]

for i, skill in enumerate(skills):
    tk.Label(input_frame, text=f"{skill}:", bg='lightblue', font=("Helvetica", 12)).grid(row=i, column=0, padx=10, pady=5)
    
    slider_label = tk.Label(input_frame, text="5", bg='lightblue', font=("Helvetica", 12))  # Default value
    slider_label.grid(row=i, column=2, padx=10, pady=5)
    
    slider = ttk.Scale(input_frame, from_=1, to=10, variable=skill_vars[i], orient='horizontal',
                       command=lambda value, lbl=slider_label: lbl.config(text=int(float(value))))  # Update label on slider change
    slider.grid(row=i, column=1, padx=10, pady=5, sticky='ew')
    slider.set(5)  # Set initial value to 5 for all sliders

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_ranking, bg='lightgreen', font=("Helvetica", 12))
submit_button.pack(pady=20)

# Labels for displaying job and courses
job_label = tk.Label(root, text="", bg='lightblue', font=("Helvetica", 12))
job_label.pack(pady=10)

courses_label = tk.Label(root, text="", bg='lightblue', font=("Helvetica", 12))
courses_label.pack(pady=10)

suitability_label = tk.Label(root, text="", bg='lightblue', font=("Helvetica", 12))
suitability_label.pack(pady=10)

# Start the GUI loop
root.mainloop()
