import bpy

# Define the collection name here
collection_name = "Collection"

# Specify the object to use as the Boolean target
boolean_target = bpy.data.objects["Cube"]

# Ensure the collection exists
if collection_name in bpy.data.collections:
    for obj in bpy.data.collections[collection_name].objects:
        if obj.type == 'MESH':  # Ensure it's a mesh object
            # Add a Boolean modifier to the object
            mod = obj.modifiers.new(name="BoolMod", type='BOOLEAN')
            mod.object = boolean_target
            mod.operation = 'DIFFERENCE'  # Can be 'UNION', 'DIFFERENCE', or 'INTERSECT'
            mod.solver = 'EXACT'  # Use the EXACT solver for Hole Tolerant option
