import bpy

# Specify the name of the collection
collection_name = "Skirts_Rounded"

# Desired settings for the Decimate modifier
planar_angle = 15  # Angle in degrees

# Find the collection by name
collection = bpy.data.collections.get(collection_name)

if collection:
    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')
    
    # Set the scene's active object to None
    bpy.context.view_layer.objects.active = None

    # Iterate over all objects in the specified collection
    for obj in collection.objects:
        # Check if the object is a mesh
        if obj.type == 'MESH':
            # Ensure the object is in the current view layer
            if obj.name not in bpy.context.view_layer.objects:
                continue

            # Select the object and make it active
            bpy.context.view_layer.objects.active = obj
            obj.select_set(True)
            
            # Add the Decimate modifier
            decimate_mod = obj.modifiers.new(name="Decimate", type='DECIMATE')
            
            # Set the modifier to Planar mode
            decimate_mod.decimate_type = 'DISSOLVE'
            
            # Set the angle limit (convert degrees to radians for the setting)
            decimate_mod.angle_limit = planar_angle * (3.14159265 / 180)
            
            # Apply the modifier
            bpy.ops.object.modifier_apply(modifier=decimate_mod.name)
            
            # Deselect the object
            obj.select_set(False)
else:
    print(f"Collection '{collection_name}' not found.")