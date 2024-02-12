import bpy
import os

# Define the base path where you want to save the .dae files
base_path = "/Users/dufok/Projects/ASAP/NN/ToSketch/"

# Make sure the base path ends with a slash
if not base_path.endswith('/'):
    base_path += '/'

# Check if the directory exists and create it if it doesn't
if not os.path.exists(base_path):
    os.makedirs(base_path)

# Loop through all collections in the current scene
for collection in bpy.data.collections:
    # Make all objects in the current collection selectable and deselect all others
    for obj in bpy.data.objects:
        obj.select_set(obj.name in collection.objects)
    
    # Define the path where the .dae file for the current collection will be saved
    file_path = os.path.join(base_path, f"{collection.name}.dae")
    
    # Export the selected objects to a .dae file
    bpy.ops.wm.collada_export(filepath=file_path, selected=True)