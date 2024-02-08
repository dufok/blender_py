import bpy

# Names of the materials to replace from and to
mat_name_to_replace = "Color1"
new_mat_name = "Color2"

# Ensure the new material exists
if new_mat_name in bpy.data.materials:
    new_mat = bpy.data.materials[new_mat_name]
else:
    print(f"Material named {new_mat_name} not found.")
    # Exit the script if the new material doesn't exist
    raise SystemExit

# Iterate through all objects in the scene
for obj in bpy.data.objects:
    # Check if the object has materials
    if obj.type == 'MESH' and obj.data.materials:
        # Replace the material
        for i, mat in enumerate(obj.data.materials):
            if mat.name == mat_name_to_replace:
                obj.data.materials[i] = new_mat
