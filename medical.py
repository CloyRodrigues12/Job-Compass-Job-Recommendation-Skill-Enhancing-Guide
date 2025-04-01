# medical.py
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from tkinter import ttk

# Medical job profiles with associated courses
job_profiles = {
    "General Practitioner": {
        "job": "General Practitioner",
        "courses": ["Clinical Skills", "Patient Care Basics", "Primary Health Care"],
    },
    "Surgeon": {
        "job": "Surgeon",
        "courses": ["Surgical Techniques", "Anatomy", "Patient Management"],
    },
    "Radiologist": {
        "job": "Radiologist",
        "courses": ["Medical Imaging", "Radiology Procedures", "Digital Imaging Processing"],
    },
    "Cardiologist": {
        "job": "Cardiologist",
        "courses": ["Cardiology Basics", "ECG Interpretation", "Cardiovascular Disorders"],
    },
    "Pharmacist": {
        "job": "Pharmacist",
        "courses": ["Pharmacology", "Medicinal Chemistry", "Drug Formulation"],
    },
    "Pathologist": {
        "job": "Pathologist",
        "courses": ["Histology", "Clinical Biochemistry", "Pathological Analysis"],
    },
    "Oncologist": {
        "job": "Oncologist",
        "courses": ["Oncology Basics", "Radiation Therapy", "Cancer Treatment"],
    },
    "Pediatrician": {
        "job": "Pediatrician",
        "courses": ["Pediatric Care", "Child Development", "Family Medicine"],
    },
    "Psychiatrist": {
        "job": "Psychiatrist",
        "courses": ["Mental Health Basics", "Psychotherapy", "Pharmacotherapy"],
    },
    "Dentist": {
        "job": "Dentist",
        "courses": ["Oral Anatomy", "Dental Hygiene", "Prosthodontics"],
    }
}

# Fuzzy Inference System for Medical Skills
def fuzzy_inference_system(skill_values):
    if skill_values[0] > 8:
        return job_profiles["General Practitioner"]
    elif skill_values[1] > 8:
        return job_profiles["Surgeon"]
    elif skill_values[2] > 8:
        return job_profiles["Radiologist"]
    elif skill_values[3] > 8:
        return job_profiles["Cardiologist"]
    elif skill_values[4] > 8:
        return job_profiles["Pharmacist"]
    elif skill_values[5] > 8:
        return job_profiles["Pathologist"]
    elif skill_values[6] > 8:
        return job_profiles["Oncologist"]
    elif skill_values[7] > 8:
        return job_profiles["Pediatrician"]
    elif skill_values[8] > 8:
        return job_profiles["Psychiatrist"]
    elif skill_values[9] > 8:
        return job_profiles["Dentist"]
    else:
        return job_profiles["General Practitioner"]

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

        # Get recommendation and calculate suitability
        profile = fuzzy_inference_system(skill_values)
        total_rank = sum(skill_values)
        suitability = (max(skill_values) / total_rank) * 100 if total_rank else 0

        # Display job and courses
        job_label.config(text=f"Recommended Job: {profile['job']}")
        courses_label.config(text="Suggested Courses: " + ", ".join(profile["courses"]))
        suitability_label.config(text=f"Suitability Percentage: {suitability:.2f}%")

        # Plot the membership graph
        plot_membership(skill_values, profile['job'])

    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))

# Function to plot the membership graph
def plot_membership(skill_values, job_title):
    x = np.arange(0, 11, 1)
    skills = ['Patient Care', 'Surgical Skills', 'Imaging Interpretation', 'Cardiology Knowledge',
              'Pharmacology', 'Pathology', 'Oncology', 'Pediatrics', 'Psychiatry', 'Dentistry']
    
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = ['blue', 'green', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'lightblue', 'lime', 'salmon']
    
    # Plotting each skill’s membership
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

# GUI Design
root = tk.Tk()
root.title("Medical Career Guide")
root.geometry("600x900")
root.configure(bg='#FF6B6B')

skills = [
    "Patient Care", "Surgical Skills", "Imaging Interpretation", "Cardiology Knowledge",
    "Pharmacology", "Pathology", "Oncology", "Pediatrics", "Psychiatry", "Dentistry"
]

skill_vars = [tk.DoubleVar() for _ in skills]

# UI setup
tk.Label(root, text="Rate your skills from 1 to 10", bg='#FF6B6B', font=("Helvetica", 14)).pack(pady=10)
input_frame = tk.Frame(root, bg='#FF6B6B')
input_frame.pack(pady=10)

for i, skill in enumerate(skills):
    tk.Label(input_frame, text=f"{skill}:", bg='#FF6B6B', font=("Helvetica", 12)).grid(row=i, column=0, padx=10, pady=5)
    
    slider_label = tk.Label(input_frame, text="5", bg='#FF6B6B', font=("Helvetica", 12))
    slider_label.grid(row=i, column=2, padx=10, pady=5)
    
    slider = ttk.Scale(input_frame, from_=1, to=10, variable=skill_vars[i], orient='horizontal',
                       command=lambda value, lbl=slider_label: lbl.config(text=int(float(value))))
    slider.grid(row=i, column=1, padx=10, pady=5, sticky='ew')
    slider.set(5)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_ranking, bg='#FF7F7F', font=("Helvetica", 12))
submit_button.pack(pady=20)

# Labels for displaying job and courses
job_label = tk.Label(root, text="", bg='#FF6B6B', font=("Helvetica", 12))
job_label.pack(pady=10)

courses_label = tk.Label(root, text="", bg='#FF6B6B', font=("Helvetica", 12))
courses_label.pack(pady=10)

suitability_label = tk.Label(root, text="", bg='#FF6B6B', font=("Helvetica", 12))
suitability_label.pack(pady=10)

# Start the GUI loop
root.mainloop()
