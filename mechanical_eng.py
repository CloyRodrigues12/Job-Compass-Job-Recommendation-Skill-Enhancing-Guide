import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from tkinter import ttk

# Expanded job profiles with associated courses for Mechanical Engineering
job_profiles = {
    "Mechanical Design Engineer": {
        "job": "Mechanical Design Engineer",
        "courses": ["SolidWorks", "Advanced CAD Techniques", "Engineering Design"],
    },
    "Manufacturing Engineer": {
        "job": "Manufacturing Engineer",
        "courses": ["Manufacturing Processes", "Lean Manufacturing", "Quality Control"],
    },
    "Project Engineer": {
        "job": "Project Engineer",
        "courses": ["Project Management", "Engineering Economics", "Risk Management"],
    },
    "HVAC Engineer": {
        "job": "HVAC Engineer",
        "courses": ["HVAC Design", "Energy Management", "Refrigeration Systems"],
    },
    "Automotive Engineer": {
        "job": "Automotive Engineer",
        "courses": ["Automotive Systems", "Vehicle Dynamics", "Powertrain Engineering"],
    },
    "Robotics Engineer": {
        "job": "Robotics Engineer",
        "courses": ["Introduction to Robotics", "Control Systems", "Robot Programming"],
    },
    "Energy Engineer": {
        "job": "Energy Engineer",
        "courses": ["Renewable Energy Systems", "Energy Management", "Sustainable Engineering"],
    },
    "Research Engineer": {
        "job": "Research Engineer",
        "courses": ["Research Methodologies", "Advanced Materials", "Product Development"],
    },
    "Quality Assurance Engineer": {
        "job": "Quality Assurance Engineer",
        "courses": ["Quality Assurance Techniques", "Statistical Process Control", "Six Sigma"],
    },
    "Thermal Engineer": {
        "job": "Thermal Engineer",
        "courses": ["Heat Transfer", "Thermal Systems Design", "Energy Conversion"],
    },
    "Materials Engineer": {
        "job": "Materials Engineer",
        "courses": ["Materials Science", "Composite Materials", "Metallurgy"],
    },
    "Maintenance Engineer": {
        "job": "Maintenance Engineer",
        "courses": ["Reliability Engineering", "Preventive Maintenance", "Condition Monitoring"],
    },
    "Systems Engineer": {
        "job": "Systems Engineer",
        "courses": ["Systems Engineering Fundamentals", "Model-Based Systems Engineering", "Requirements Engineering"],
    },
    "Aerospace Engineer": {
        "job": "Aerospace Engineer",
        "courses": ["Aerodynamics", "Aircraft Structures", "Propulsion Systems"],
    },
    "Design Engineer": {
        "job": "Design Engineer",
        "courses": ["Computer-Aided Design (CAD)", "3D Modeling", "Finite Element Analysis"],
    },
}

# Fuzzy Inference System Implementation
def fuzzy_inference_system(skill_values):
    if skill_values[0] > 8:  # High ranking in CAD
        return job_profiles["Design Engineer"]
    elif skill_values[1] > 8:  # High ranking in Manufacturing Techniques
        return job_profiles["Manufacturing Engineer"]
    elif skill_values[2] > 7:  # Strong in Project Management
        return job_profiles["Project Engineer"]
    elif skill_values[3] > 7:  # Strong in HVAC Systems
        return job_profiles["HVAC Engineer"]
    elif skill_values[4] > 7:  # Strong in Automotive Systems
        return job_profiles["Automotive Engineer"]
    elif skill_values[5] > 7:  # Strong in Robotics
        return job_profiles["Robotics Engineer"]
    elif skill_values[6] > 7:  # Strong in Renewable Energy
        return job_profiles["Energy Engineer"]
    elif skill_values[7] > 7:  # Strong in Research and Development
        return job_profiles["Research Engineer"]
    elif skill_values[8] > 7:  # Strong in Quality Assurance
        return job_profiles["Quality Assurance Engineer"]
    elif skill_values[9] > 7:  # Strong in Thermodynamics
        return job_profiles["Thermal Engineer"]
    elif skill_values[0] > 6:  # Strong in Maintenance
        return job_profiles["Maintenance Engineer"]
    elif skill_values[1] > 6:  # Strong in Systems Engineering
        return job_profiles["Systems Engineer"]
    elif skill_values[2] > 6:  # Strong in Aerospace
        return job_profiles["Aerospace Engineer"]
    else:
        return job_profiles["Mechanical Design Engineer"]

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
        for var in [cad_var, manufacturing_tech_var, project_management_var, 
                    hvac_var, automotive_sys_var, robotics_var, 
                    renewable_energy_var, research_dev_var, 
                    quality_assurance_var, thermodynamics_var]:
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
    skills = ['CAD Skills', 'Manufacturing Techniques', 'Project Management', 'HVAC Systems',
              'Automotive Systems', 'Robotics', 'Renewable Energy', 'Research & Development',
              'Quality Assurance', 'Thermodynamics']

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

# GUI
# Function to update the label with the current slider value
def update_label(slider_var, label):
    label.config(text=f"{int(slider_var.get())}")  # Update label with the current value

# Set up the main window
root = tk.Tk()
root.title("Mechanical Engineering Career Guide")
root.geometry("600x900")  # Increased window size
root.configure(bg='#81C784')  # Light color background

# Skill ranking inputs
cad_var = tk.DoubleVar()
manufacturing_tech_var = tk.DoubleVar()
project_management_var = tk.DoubleVar()
hvac_var = tk.DoubleVar()
automotive_sys_var = tk.DoubleVar()
robotics_var = tk.DoubleVar()
renewable_energy_var = tk.DoubleVar()
research_dev_var = tk.DoubleVar()
quality_assurance_var = tk.DoubleVar()
thermodynamics_var = tk.DoubleVar()

# Skill ranking labels and inputs
tk.Label(root, text="Rate your skills from 1 to 10", bg='#81C784', font=("Helvetica", 14)).pack(pady=10)

# Create a frame to hold the sliders
input_frame = tk.Frame(root, bg='#81C784')
input_frame.pack(pady=10)

skills = [
    "CAD Skills",
    "Manufacturing Techniques",
    "Project Management",
    "HVAC Systems",
    "Automotive Systems",
    "Robotics",
    "Renewable Energy",
    "Research & Development",
    "Quality Assurance",
    "Thermodynamics",
]

skill_vars = [
    cad_var,
    manufacturing_tech_var,
    project_management_var,
    hvac_var,
    automotive_sys_var,
    robotics_var,
    renewable_energy_var,
    research_dev_var,
    quality_assurance_var,
    thermodynamics_var,
]

for i, skill in enumerate(skills):
    tk.Label(input_frame, text=f"{skill}:", bg='#81C784', font=("Helvetica", 12)).grid(row=i, column=0, padx=10, pady=5)
    
    slider_label = tk.Label(input_frame, text="5", bg='#81C784', font=("Helvetica", 12))  # Default value
    slider_label.grid(row=i, column=2)

    slider = tk.Scale(input_frame, from_=1, to=10, orient=tk.HORIZONTAL, variable=skill_vars[i],
                      command=lambda val, label=slider_label: update_label(skill_vars[i], label))
    slider.grid(row=i, column=1)

# Submit button
submit_btn = tk.Button(root, text="Submit Rankings", command=submit_ranking, bg='#4CAF50', font=("Helvetica", 12))
submit_btn.pack(pady=20)

# Labels for displaying results
job_label = tk.Label(root, text="", bg='#81C784', font=("Helvetica", 14))
job_label.pack(pady=10)

courses_label = tk.Label(root, text="", bg='#81C784', font=("Helvetica", 12))
courses_label.pack(pady=10)

suitability_label = tk.Label(root, text="", bg='#81C784', font=("Helvetica", 12))
suitability_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
