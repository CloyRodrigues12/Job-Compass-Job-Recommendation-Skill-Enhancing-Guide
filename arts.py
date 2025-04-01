import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from tkinter import ttk

# Job profiles with associated courses for Arts & Design
job_profiles = {
    "Graphic Designer": {
        "job": "Graphic Designer",
        "courses": ["Graphic Design Fundamentals", "Adobe Creative Suite", "Color Theory"],
    },
    "UX Researcher": {
        "job": "UX Researcher",
        "courses": ["User Research Methods", "Data Analysis for UX", "Usability Testing"],
    },
    "Motion Graphic Designer": {
        "job": "Motion Graphic Designer",
        "courses": ["Animation Techniques", "Adobe After Effects", "Visual Storytelling"],
    },
    "Fine Artist": {
        "job": "Fine Artist",
        "courses": ["Painting Techniques", "Sculpture Fundamentals", "Art History"],
    },
    "Commercial Photographer": {
        "job": "Commercial Photographer",
        "courses": ["Photography Basics", "Lighting Techniques", "Post-Processing"],
    },
    "Fashion Designer": {
        "job": "Fashion Designer",
        "courses": ["Fashion Illustration", "Textile Design", "Trend Forecasting"],
    },
    "Interior Designer": {
        "job": "Interior Designer",
        "courses": ["Interior Design Principles", "Space Planning", "Color Theory for Interiors"],
    },
    "Game Artist": {
        "job": "Game Artist",
        "courses": ["Character Design", "Environment Art", "3D Modeling for Games"],
    },
    "Web Designer": {
        "job": "Web Designer",
        "courses": ["HTML & CSS", "JavaScript Basics", "Responsive Design"],
    },
    "Art Curator": {
        "job": "Art Curator",
        "courses": ["Art Curation Basics", "Gallery Management", "Exhibition Design"],
    },
}

# Fuzzy Inference System Implementation
def fuzzy_inference_system(skill_values):
    if skill_values[0] > 8:  # High ranking in Graphic Design
        return job_profiles["Graphic Designer"]
    elif skill_values[1] > 8:  # High ranking in UX Research
        return job_profiles["UX Researcher"]
    elif skill_values[2] > 7:  # Strong in Motion Graphics
        return job_profiles["Motion Graphic Designer"]
    elif skill_values[3] > 7:  # Strong in Fine Arts
        return job_profiles["Fine Artist"]
    elif skill_values[4] > 7:  # Strong in Photography
        return job_profiles["Commercial Photographer"]
    elif skill_values[5] > 7:  # Strong in Fashion Design
        return job_profiles["Fashion Designer"]
    elif skill_values[6] > 7:  # Strong in Interior Design
        return job_profiles["Interior Designer"]
    elif skill_values[7] > 7:  # Strong in Game Art Design
        return job_profiles["Game Artist"]
    elif skill_values[8] > 7:  # Strong in Web Design
        return job_profiles["Web Designer"]
    elif skill_values[9] > 7:  # Strong in Art Curation
        return job_profiles["Art Curator"]
    else:
        return job_profiles["Graphic Designer"]  # Default recommendation

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
        for var in [graphic_design_var, uiux_design_var, illustration_var, 
                    photography_var, animation_var, video_production_var, 
                    art_direction_var, branding_var, web_design_var, 
                    fine_arts_var]:
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
    skills = ['Graphic Design', 'UI/UX Design', 'Illustration', 'Photography',
              'Animation', 'Video Production', 'Art Direction', 'Branding',
              'Web Design', 'Fine Arts']
    
    fig, ax = plt.subplots(figsize=(10, 6))

    colors = ['#FF6347', '#FF4500', '#FFD700', '#ADFF2F', '#00CED1', 
              '#4682B4', '#9370DB', '#8B0000', '#FF69B4', '#B22222']
    
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
root.title("Arts & Design Career Guide")
root.geometry("600x900")  # Increased window size
root.configure(bg='#FFB3BA')  # Light coral background

# Skill ranking inputs
graphic_design_var = tk.DoubleVar()
uiux_design_var = tk.DoubleVar()
illustration_var = tk.DoubleVar()
photography_var = tk.DoubleVar()
animation_var = tk.DoubleVar()
video_production_var = tk.DoubleVar()
art_direction_var = tk.DoubleVar()
branding_var = tk.DoubleVar()
web_design_var = tk.DoubleVar()
fine_arts_var = tk.DoubleVar()

# Skill ranking labels and inputs
tk.Label(root, text="Rate your skills from 1 to 10", bg='#FFB3BA', font=("Helvetica", 14)).pack(pady=10)

# Create a frame to hold the sliders
input_frame = tk.Frame(root, bg='#FFB3BA')
input_frame.pack(pady=10)

skills = [
    "Graphic Design",
    "UI/UX Design",
    "Illustration",
    "Photography",
    "Animation",
    "Video Production",
    "Art Direction",
    "Branding",
    "Web Design",
    "Fine Arts"
]

skill_vars = [
    graphic_design_var,
    uiux_design_var,
    illustration_var,
    photography_var,
    animation_var,
    video_production_var,
    art_direction_var,
    branding_var,
    web_design_var,
    fine_arts_var
]

for i, skill in enumerate(skills):
    tk.Label(input_frame, text=f"{skill}:", bg='#FFB3BA', font=("Helvetica", 12)).grid(row=i, column=0, padx=10, pady=5)
    
    slider_label = tk.Label(input_frame, text="5", bg='#FFB3BA', font=("Helvetica", 12))  # Default value
    slider_label.grid(row=i, column=2, padx=10, pady=5)
    
    slider = ttk.Scale(input_frame, from_=1, to=10, variable=skill_vars[i], orient='horizontal',
                       command=lambda value, lbl=slider_label: lbl.config(text=int(float(value))))  # Update label on slider move
    slider.grid(row=i, column=1, padx=10, pady=5)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_ranking, bg="#FF6347", fg="white", font=("Helvetica", 12))
submit_button.pack(pady=20)

# Labels for displaying recommendations
job_label = tk.Label(root, text="", bg='#FFB3BA', font=("Helvetica", 14))
job_label.pack(pady=10)

courses_label = tk.Label(root, text="", bg='#FFB3BA', font=("Helvetica", 12))
courses_label.pack(pady=10)

suitability_label = tk.Label(root, text="", bg='#FFB3BA', font=("Helvetica", 12))
suitability_label.pack(pady=10)

# Start the GUI loop
root.mainloop()
