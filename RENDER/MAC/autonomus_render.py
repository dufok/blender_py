#!/usr/bin/env python3

import subprocess

# Define the path to the Blender application
blender_path = "/Applications/Blender\ 4.0.app/Contents/MacOS/Blender"


# Define the base path for the projects
project_base_path = "/Users/dufok/Projects/ASAP/WEY/Models_Render"
project_script_path="/Users/dufok/Projects/Blender_scripts"

# Define a dictionary that maps blend files to their corresponding Python scripts
blend_files_to_scripts = {
    "WEY_LOUNG.blend": "background_render_loung.py",
    "WEY_LOUNG2.blend": "background_render_loung2.py",
    "WEY_Recieb.blend": "background_render_Recib.py",
    "WEY_Enterence.blend": "background_render_Enterence.py",
}

# Loop through the dictionary
for blend_file, python_script in blend_files_to_scripts.items():
    print(f"Starting render for {blend_file} using {python_script}...")
    subprocess.run(f'{blender_path} "{project_base_path}/{blend_file}" --background --python "{project_script_path}/{python_script}"', shell=True)