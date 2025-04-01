import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from tkinter import ttk

# Expanded job profiles with associated courses for Civil Engineering
job_profiles = {
    "Construction Project Engineer": {
        "job": "Construction Project Engineer",
        "courses": ["Construction Management", "Risk Management in Projects", "Building Codes and Standards"],
    },
    "Water Resources Engineer": {
        "job": "Water Resources Engineer",
        "courses": ["Hydrology and Water Resources", "Water Quality Management", "Irrigation Engineering"],
    },
    "Seismic Engineer": {
        "job": "Seismic Engineer",
        "courses": ["Earthquake Engineering", "Structural Dynamics", "Risk Assessment in Seismic Design"],
    },
    "Materials Engineer": {
        "job": "Materials Engineer",
        "courses": ["Construction Materials", "Material Testing and Evaluation", "Advanced Materials for Construction"],
    },
    "Coastal Engineer": {
        "job": "Coastal Engineer",
        "courses": ["Coastal Engineering", "Oceanography", "Hydraulics of Coastal Structures"],
    },
    "Environmental Compliance Specialist": {
        "job": "Environmental Compliance Specialist",
        "courses": ["Environmental Regulations", "Sustainable Development", "Impact Assessment Techniques"],
    },
    "Land Development Engineer": {
        "job": "Land Development Engineer",
        "courses": ["Site Development", "Land Surveying", "Site Planning and Design"],
    },
    "Railway Engineer": {
        "job": "Railway Engineer",
        "courses": ["Railway Engineering", "Transportation Planning", "Track Design and Maintenance"],
    },
    "Forensic Engineer": {
        "job": "Forensic Engineer",
        "courses": ["Forensic Engineering Principles", "Failure Analysis", "Legal Aspects of Engineering"],
    },
    "Bridge Engineer": {
        "job": "Bridge Engineer",
        "courses": ["Bridge Engineering", "Structural Design", "Load Rating of Bridges"],
    },
}

# Fuzzy Inference System Implementation
def fuzzy_inference_system(skill_values):
    if skill_values[0] > 8:  # High ranking in Structural Analysis
        return job_profiles["Construction Project Engineer"]
    elif skill_values[1] > 8:  # High ranking in Water Resources
        return job_profiles["Water Resources Engineer"]
    elif skill_values[2] > 7:  # Strong in Seismic Design
        return job_profiles["Seismic Engineer"]
    elif skill_values[3] > 7:  # Strong in Material Science
        return job_profiles["Materials Engineer"]
    elif skill_values[4] > 7:  # Strong in Coastal Engineering
        return job_profiles["Coastal Engineer"]
    elif skill_values[5] > 7:  # Strong in Environmental Engineering
        return job_profiles["Environmental Compliance Specialist"]
    elif skill_values[6] > 7:  # Strong in Land Development
        return job_profiles["Land Development Engineer"]
    elif skill_values[7] > 7:  # Strong in Transportation
        return job_profiles["Railway Engineer"]
    elif skill_values[8] > 7:  # Strong in Forensics
        return job_profiles["Forensic Engineer"]
    elif skill_values[9] > 7:  # Strong in Structural Engineering
        return job_profiles["Bridge Engineer"]
    else:
        return job_profiles["Construction Project Engineer"]  # Default case

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
        for var in [structural_analysis_var, water_resources_var, seismic_design_var, 
                    materials_science_var, coastal_engineering_var, environmental_engineering_var, 
                    land_development_var, transportation_var, forensics_var, structural_engineering_var]:
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
    skills = ['Structural Analysis', 'Water Resources', 'Seismic Design', 
              'Materials Science', 'Coastal Engineering', 'Environmental Engineering', 
              'Land Development', 'Transportation', 'Forensics', 'Structural Engineering']
    
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

# GUIS
# Function to update the label with the current slider value
def update_label(slider_var, label):
    label.config(text=f"{int(slider_var.get())}")  # Update label with the current value

# Set up the main window
root = tk.Tk()
root.title("Civil Engineering Career Guide")
root.geometry("600x900")  # Increased window size
root.configure(bg='#F6E58D')  # Light green color background

# Skill ranking inputs
structural_analysis_var = tk.DoubleVar()
water_resources_var = tk.DoubleVar()
seismic_design_var = tk.DoubleVar()
materials_science_var = tk.DoubleVar()
coastal_engineering_var = tk.DoubleVar()
environmental_engineering_var = tk.DoubleVar()
land_development_var = tk.DoubleVar()
transportation_var = tk.DoubleVar()
forensics_var = tk.DoubleVar()
structural_engineering_var = tk.DoubleVar()

# Skill ranking labels and inputs
tk.Label(root, text="Rate your skills from 1 to 10", bg='#F6E58D', font=("Helvetica", 14)).pack(pady=10)

# Create a frame to hold the sliders
input_frame = tk.Frame(root, bg='#F6E58D')
input_frame.pack(pady=10)

skills = [
    "Structural Analysis",
    "Water Resources",
    "Seismic Design",
    "Materials Science",
    "Coastal Engineering",
    "Environmental Engineering",
    "Land Development",
    "Transportation",
    "Forensics",
    "Structural Engineering"
]

skill_vars = [
    structural_analysis_var,
    water_resources_var,
    seismic_design_var,
    materials_science_var,
    coastal_engineering_var,
    environmental_engineering_var,
    land_development_var,
    transportation_var,
    forensics_var,
    structural_engineering_var
]

for i, skill in enumerate(skills):
    tk.Label(input_frame, text=f"{skill}:", bg='#F6E58D', font=("Helvetica", 12)).grid(row=i, column=0, padx=10, pady=5)
    
    slider_label = tk.Label(input_frame, text="5", bg='#F6E58D', font=("Helvetica", 12))  # Default value
    slider_label.grid(row=i, column=2, padx=10, pady=5)
    
    slider = ttk.Scale(input_frame, from_=1, to=10, variable=skill_vars[i], orient='horizontal',
                       command=lambda value, lbl=slider_label: lbl.config(text=int(float(value))))  # Update label on slider change
    slider.grid(row=i, column=1, padx=10, pady=5, sticky='ew')
    slider.set(5)  # Set initial value to 5 for all sliders

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_ranking, bg='#FFD700', font=("Helvetica", 12))
submit_button.pack(pady=20)

# Labels for displaying job and courses
job_label = tk.Label(root, text="", bg='#F6E58D', font=("Helvetica", 12))
job_label.pack(pady=10)

courses_label = tk.Label(root, text="", bg='#F6E58D', font=("Helvetica", 12))
courses_label.pack(pady=10)

suitability_label = tk.Label(root, text="", bg='#F6E58D', font=("Helvetica", 12))
suitability_label.pack(pady=10)

# Start the main event loop
root.mainloop()
