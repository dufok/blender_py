import bpy

# Name of the existing emission material
material_name = "Mask_Black"  # Make sure this matches your material's name exactly

# Name of the collection you want to apply the material to
collection_name = "YourCollectionName"  # Replace with your collection name

# Check if the material exists
if material_name in bpy.data.materials:
    mat = bpy.data.materials[material_name]
else:
    print(f"Material '{material_name}' not found.")
    mat = None

# If the material was found, assign it to all objects in the specified collection
if mat:
    for obj in bpy.data.collections[collection_name].all_objects:
        if obj.type == 'MESH':  # Only apply to mesh objects
            # Clear existing materials
            obj.data.materials.clear()
            # Assign the "Mask_Black" material
            obj.data.materials.append(mat)
    print(f"Material '{material_name}' applied to all objects in '{collection_name}'.")
else:
    print("Operation aborted. Correct material name or create it.")
