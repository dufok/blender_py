import bpy

# The name of the material to remove
material_to_remove = "MaterialToRemove"

# Iterate through all objects in the scene
for obj in bpy.data.objects:
    # Check if the object is a mesh and has materials
    if obj.type == 'MESH' and obj.data.materials:
        # Loop over all material slots and remove the specified material
        for slot in obj.material_slots:
            if slot.material and slot.material.name == material_to_remove:
                # Remove the material from the slot
                obj.data.materials.pop(index=slot.material_index, update_data=True)
